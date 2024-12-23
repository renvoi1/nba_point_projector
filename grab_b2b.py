import pandas as pd
from nba_api.stats.endpoints import playergamelog, teamgamelog, leaguedashteamstats, playercareerstats, commonplayerinfo
from nba_api.stats.static import players, teams
import requests
from datetime import datetime
from io import StringIO
from bs4 import BeautifulSoup

# Step 1: Grab the Team ID
def grab_last_game(player_id):
    nba_teams = teams.get_teams()
    player_info = commonplayerinfo.CommonPlayerInfo(player_id=player_id)
    player_data = player_info.get_data_frames()[0]
    team_name = player_data["TEAM_ABBREVIATION"].iloc[0]
    team_info = next((team for team in nba_teams if team["abbreviation"] == team_name), None)
    team_id = team_info["id"]

    # Step 2: Fetch the Team's Game Log for the Current Season
    season = "2024-25" 
    gamelog = teamgamelog.TeamGameLog(team_id=team_id, season=season)
    gamelog_df = gamelog.get_data_frames()[0]

    

    # Step 3: Sort by Game Date to Get the Most Recent Game
    gamelog_df["GAME_DATE"] = pd.to_datetime(gamelog_df["GAME_DATE"], format='%b %d, %Y')  # Convert to datetime
    last_game = gamelog_df.sort_values("GAME_DATE", ascending=False).iloc[0]  # Get the most recent game
    global last_game_date
    last_game_date = last_game['GAME_DATE'].strftime('%Y-%m-%d')
    print(f'last played game is {last_game_date}')

    
# may or may not remove this due to not recognizing b2b games unless one of said games is happening day of