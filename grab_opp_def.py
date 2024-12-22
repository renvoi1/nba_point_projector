import pandas as pd
from nba_api.stats.endpoints import playergamelog, teamgamelog, leaguedashteamstats, playercareerstats
from nba_api.stats.static import players, teams
import requests
from datetime import datetime
from io import StringIO
from bs4 import BeautifulSoup

def grab_opp(player_id):
    season = '2024-25'
    team_stats = leaguedashteamstats.LeagueDashTeamStats(season=season, measure_type_detailed_defense="Advanced")

    gamelog = playergamelog.PlayerGameLog(player_id=player_id, season=season)


    df = gamelog.get_data_frames()[0]

    stats_df = team_stats.get_data_frames()[0]

    # Optional: Filter for a specific team
    from grab_team_schedule import next_game
    opp = next_game['Opponent']
    team_def_rating = stats_df.loc[stats_df["TEAM_NAME"] == (opp), "DEF_RATING"]
    team_def_reb = stats_df.loc[stats_df["TEAM_NAME"] == (opp), "DREB_PCT"]
    def_rating = team_def_rating.values[0]
    def_reb = team_def_reb.values[0]


    if not team_def_rating.empty:
        print(f"Defensive Rating for {opp} in {season}: {team_def_rating.values[0]}")
    else:
        print(f"{opp} stats not found for {season}.")

    if not team_def_reb.empty:
        print(f"Defensive rebound for {opp} in {season}: {team_def_reb.values[0]}")
