from selenium import webdriver
import datetime
import requests
import json


def getChessNotation(game_url=""):
    """Scrape chess notation from chess.com using Selenium."""

    # Grab HTML
    PATH = "/home/lucas/Downloads"
    driver = webdriver.Chrome(PATH)

    URL = "https://www.chess.com/game/live/36227889133"
    driver.get(URL)


def main():

    # Find month and year
    date = datetime.datetime.now()
    year = date.year
    # month = date.strftime("%m")
    month = "01"
    print(year, month)

    # URL for archived games 
    URL = f"https://api.chess.com/pub/player/zzdxk/games/{year}/{month}"
    # Data from Chess.com API
    data = requests.get(URL).json()
    game_metadata = data["games"]
    # Store game IDs and URL
    past_games = {}
    for i, game in enumerate(game_metadata):
        game_id = str(game["url"][-1:-11:-1])
        game_link = game["url"]
        past_games[game_id] = game_link

    # Get chess moves
    for key, val in past_games.items():
        print(key, val)


if __name__ == "__main__":
    getChessNotation()
    # main();

