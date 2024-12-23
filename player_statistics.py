import pandas as pd
from nba_api.stats.endpoints import playergamelog, teamgamelog, leaguedashteamstats, playercareerstats
from nba_api.stats.static import players, teams
import requests
from datetime import datetime
from io import StringIO
from bs4 import BeautifulSoup

# function definition
def grab_player_stats(guy):
    # define basic variables, season, player, etc.
    all_players = players.get_players()
    season = '2024-25'  
    player = [player for player in all_players if player['full_name'] == guy][0]
    player_id = player['id']

    gamelog = playergamelog.PlayerGameLog(player_id=player_id, season=season)
    df = gamelog.get_data_frames()[0]
    # set data to var for easy access later on
    ppg = df['PTS'].mean()
    mpg = df['MIN'].mean()
    fga = df['FGA'].mean()
    # print
    print(f'ppg = {ppg}')
    print(f'mpg = {mpg}')
    print(f'fga = {fga}')
