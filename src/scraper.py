from selenium import webdriver
from selenium.webdriver.common.by import By

import datetime
import requests
import json
import io
import chessdotcom_export
import chess.pgn
import chessdotcom


def getPlayerProfile():
    reponse = chessdotcom.get_player_profile('zzdxk')
    player_name = response.player.name
    print(player_name)


def getChessNotation(url=''):
    """Extract chess notation using chessdotcom_export library."""

    # # Extract game data from chessdotcom API
    # matches = list(map(lambda j: chessdotcom_export.Game.from_api_response(j), chessdotcom_export.get_player_games('zzdxk')))
    # # Game zero
    # game = matches[0]
    # print(game.url)
    # # Display game ID
    # game_url = game.url[-1:-11:-1]
    # print(game_url)
    # # Display game 0 chess notation
    # game_movelist = chess.pgn.read_game(io.StringIO(game.pgn))
    # for move in game_movelist.mainline_moves():
    #     print(move)

    # Use chessdotcom API to grab monthly games in pgn format
    montly_matches = chessdotcom.client.get_player_games_by_month_pgn('zzdxk', 2022, 2)
    print(month_matches)


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
    getPlayerProfile()
    # getChessNotation()
    # main();

