from nba_api.stats.endpoints import teamgamelog
from nba_api.stats.static import teams
import pandas as pd

# Step 1: Find the Team ID
team_name = "Golden State Warriors"
nba_teams = teams.get_teams()
team_info = next((team for team in nba_teams if team["full_name"] == team_name), None)

if team_info:
    team_id = team_info["id"]
    print(f"Team ID for {team_name}: {team_id}")

    # Step 2: Fetch Team Game Log
    season = "2024-25"  # Specify the season
    gamelog = teamgamelog.TeamGameLog(team_id=team_id, season=season)
    gamelog_df = gamelog.get_data_frames()[0]

    # Step 3: Sort Games by Date
    gamelog_df["GAME_DATE"] = pd.to_datetime(gamelog_df["GAME_DATE"])  # Convert to datetime
    last_game = gamelog_df.sort_values("GAME_DATE", ascending=False).iloc[0]  # Most recent game

    # Step 4: Display Last Game Details
    print(f"Last game played by {team_name}:")
    print(f"Date: {last_game['GAME_DATE'].date()}")
    print(f"Matchup: {last_game['MATCHUP']}")
else:
    print(f"Team {team_name} not found.")
