Dino Bot (Selenium)

Projekt demonstruje umiejętności automatyzacji (Selenium + JS injection) oraz podejście testerskie, w tym walidacje, raportowanie, logowanie i tworzenie screenshotów. Prezentuje również umiejętność pracy z przejrzystą strukturą repozytorium w kontekście QA/Automation.

Automatyzacja klasycznej gry "Chrome Dino" z wykorzystaniem Selenium WebDriver.  

Wymagania:
- Python 3.10+ (testowane na 3.11)
- Google Chrome (ta sama wersja co ChromeDriver)
- ChromeDriver w PATH
- Pakiety Python z pliku `requirements.txt`:
  ```bash
  pip install -r requirements.txt


Uruchomienie:

bash
	#klonowanie repozytorium
	git clone https://github.com/Michal821/Dino-bot.git
	cd Dino-bot

	#tworzenie i aktywacja środowiska wirtualnego
	python -m venv venv
	# Windows
	venv\Scripts\activate
	# Linux/Mac
	source venv/bin/activate

	#instalacja zależności
	pip install -r requirements.txt

	#uruchomienie
	python dino_bot.py


Funkcjonalności:
	Automatyczne sterowanie Dino w grze chromedino.com . 
	Reagowanie na przeszkody (xPos < threshold). 
	Liczenie ominiętych przeszkód i przebiegniętego dystansu. 
	Powtarzanie gry określoną liczbę razy (domyślnie 5). 
	Raport wyników w formacie CSV (results.csv). 
	Screenshoty po każdej grze w folderze screenshots/.


Przykładowe logi w folderze console logs.



