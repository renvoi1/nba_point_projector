# imports
import pandas as pd
from nba_api.stats.endpoints import playergamelog, teamgamelog, leaguedashteamstats, playercareerstats
from nba_api.stats.static import players, teams
import requests
from datetime import datetime
from io import StringIO
from bs4 import BeautifulSoup
from player_statistics import grab_player_stats
from grab_team_schedule import grab_team_sch
from grab_opp_def import grab_opp
from grab_b2b import grab_last_game


# Ask for player name, then outsource all stat grabs to dif files (this is the only reason this file eists)
all_teams = teams.get_teams()
all_players = players.get_players()
while True:
    try:
        guy2 = input("Please input player (case sens): ")
        player = [player for player in all_players if player['full_name'] == guy2][0]
        break
    except IndexError:
        print('player does not exist/wrong case')
grab_player_stats(guy=guy2)
# need player id for team related stat grabs
player = [player for player in all_players if player['full_name'] == guy2][0]
player_id = player['id']
# call funcs
grab_team_sch(player_id=player_id)
grab_opp(player_id=player_id)
grab_last_game(player_id=player_id)

