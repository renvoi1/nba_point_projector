import pandas as pd
from nba_api.stats.endpoints import playergamelog, teamgamelog, leaguedashteamstats, playercareerstats
from nba_api.stats.static import players, teams
import requests
from datetime import datetime
from io import StringIO
from bs4 import BeautifulSoup


def grab_player_stats(guy):

    all_players = players.get_players()
    season = '2024-25'  
    player = [player for player in all_players if player['full_name'] == guy][0]
    player_id = player['id']

    gamelog = playergamelog.PlayerGameLog(player_id=player_id, season=season)
    df = gamelog.get_data_frames()[0]

    ppg = df['PTS'].mean()
    mpg = df['MIN'].mean()
    fga = df['FGA'].mean()

    print(f'ppg = {ppg}')
    print(f'mpg = {mpg}')
    print(f'fga = {fga}')
