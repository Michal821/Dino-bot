import csv
import os
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class DinoBot:
    def __init__(self, games_to_play=5, jump_threshold=120):
        self.games_to_play = games_to_play
        self.jump_threshold = jump_threshold
        self.results_file = "results.csv"

        # creating a folder
        os.makedirs("screenshots", exist_ok=True)

        # Configuration Selenium
        options = webdriver.ChromeOptions()
        options.add_argument("--mute-audio")
        self.driver = webdriver.Chrome(options=options)

        # Open the game
        self.driver.get("https://chromedino.com/")
        time.sleep(2)

        self.body = self.driver.find_element(By.TAG_NAME, "body")

        # Creating a CSV file
        if not os.path.exists(self.results_file):
            with open(self.results_file, mode="w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["Game", "ObstaclesCleared", "Distance", "Timestamp"])

    def play(self):
        """Play Dino Games"""
        for game in range(1, self.games_to_play + 1):
            print(f"\n=== Game {game}/{self.games_to_play} ===")
            obstacles_cleared = 0

            # Start
            self.body.send_keys(Keys.SPACE)
            time.sleep(0.5)

            while True:
                try:
                    # Obstacle
                    obstacles = self.driver.execute_script(
                        "return Runner.instance_.horizon.obstacles"
                    )

                    if obstacles:
                        obstacle_x = obstacles[0]["xPos"]

                        if obstacle_x < self.jump_threshold:
                            self.body.send_keys(Keys.ARROW_UP)
                            obstacles_cleared += 1
                            distance = self.driver.execute_script(
                                "return Math.floor(Runner.instance_.distanceRan)"
                            )
                            print(
                                f"Jump, obstacle missed: {obstacles_cleared}, distance: {distance}"
                            )

                    # End game decetion
                    crashed = self.driver.execute_script("return Runner.instance_.crashed")
                    if crashed:
                        distance = self.driver.execute_script(
                            "return Math.floor(Runner.instance_.distanceRan)"
                        )
                        print(
                            f"END – {obstacles_cleared} objects skipped, distance: {distance}"
                        )

                        # Screenshot
                        screenshot_name = f"screenshots/game_{game}.png"
                        self.driver.save_screenshot(screenshot_name)
                        print(f"Screenshot saved: {screenshot_name}")

                        # Save CSV
                        with open(self.results_file, mode="a", newline="") as f:
                            writer = csv.writer(f)
                            writer.writerow(
                                [game, obstacles_cleared, distance, datetime.now()]
                            )
                        break

                    time.sleep(0.05)

                except Exception as e:
                    print(f"error? {game}: {e}")
                    break

            # Restart the game
            self.driver.execute_script("Runner.instance_.restart()")
            time.sleep(1)

    def quit(self):
        self.driver.quit()


if __name__ == "__main__":
    bot = DinoBot(games_to_play=5, jump_threshold=120)
    bot.play()
    bot.quit()
    print("\n=== End game ===")