Dino Bot (Selenium)

This project demonstrates automation skills (Selenium + JS injection) and a testing approach, including validation, reporting, logging, and screenshot creation. 
It also demonstrates the ability to work with a clear repository structure in a QA/Automation context.

Automation of the classic "Chrome Dino" game using Selenium WebDriver.

Requirements:
- Python 3.10+ (tested on 3.11)
- Google Chrome (same version as ChromeDriver)
- ChromeDriver in the PATH
- Python packages from the `requirements.txt` file:
```bash
pip install -r requirements.txt

Runtime:
python dino_bot.py

Features:

Automatic control of Dino in the chromedino.com game.
Response to obstacles (xPos < threshold).
Tracks obstacles avoided and distance traveled.
Repeats the game a specified number of times (default: 5).
Results report in CSV format (results.csv).
Screenshots after each game in the screenshots/ folder.

Sample logs in the console logs folder.


