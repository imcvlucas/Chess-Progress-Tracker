from selenium import webdriver
from selenium.webdriver.common.by import By

import datetime
import requests
import json
import io
import chessdotcom_export
import chess.pgn


def getChessNotation(url=''):
    """Extract chess notation using chessdotcom_export library."""

    # Extract game data from chessdotcom API
    matches = list(map(lambda j: chessdotcom_export.Game.from_api_response(j), chessdotcom_export.get_player_games('zzdxk')))
    # Extract pgn 
    games = matches[0].pgn
    # Display game ID
    game_url = matches[0].url[-1:-11:-1]
    print(game_url)
    # Display game 0 chess notation
    game_movelist = chess.pgn.read_game(io.StringIO(games))
    for move in game_movelist.mainline_moves():
        print(move)


def main():

    # Find month and year
    date = datetime.datetime.now()
    year = date.year
    # month = date.strftime("%m")
    month = "01"
    print(year, month)

    # URL for archived games 
    URL = f"https://api.chess.com/pub/player/zzdxk/games/{year}/{month}"
    # Grab JSON from Chess.com API
    data = requests.get(URL).json()
    game_metadata = data["games"]

    # Store game IDs and URL
    past_games = {}
    for i, game in enumerate(game_metadata):
        game_id = str(game["url"][-1:-11:-1])
        game_link = game["url"]
        past_games[game_id] = game_link

    # Get chess moves
    for game_id, game_link in past_games.items():
        print(game_id, game_link)


if __name__ == "__main__":
    getChessNotation()
    # main();

