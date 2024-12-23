import pandas as pd
from nba_api.stats.endpoints import playergamelog, teamgamelog, leaguedashteamstats, playercareerstats
from nba_api.stats.static import players, teams
import requests
from datetime import datetime
from io import StringIO
from bs4 import BeautifulSoup

# define function
def grab_team_sch(player_id):
    global next_game
    career_stats = playercareerstats.PlayerCareerStats(player_id=player_id)
    df2 = career_stats.get_data_frames()[0]

    # URL for specified team schedule
    global team_abbreviation
    team_abbreviation = df2.iloc[-1]["TEAM_ABBREVIATION"]
    season_year = 2025
    schedule_url = f"https://www.basketball-reference.com/teams/{team_abbreviation}/{season_year}_games.html"

    # Fetch the page content
    response = requests.get(schedule_url)
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the schedule table
    schedule_table = soup.find("table", {"id": "games"})

    if schedule_table:
        # Read the table into a DataFrame
        df = pd.read_html(StringIO(str(schedule_table)))[0]
        
        # Drop rows where the "Date" column is NaN or invalid
        df = df[df["Date"].notna()]  # Remove rows where the "Date" is NaN
        
        # Ensure "Date" column contains valid date formats
        valid_dates = []
        for date in df["Date"]:
            try:
                valid_dates.append(datetime.strptime(date, "%a, %b %d, %Y"))  # Basketball Reference's date format
            except ValueError:
                valid_dates.append(None)
        
        # Replace the "Date" column with valid parsed dates
        df["Date"] = valid_dates
        df = df[df["Date"].notna()]  # Drop rows with invalid dates
        
        # Convert the "Date" column to datetime
        df["Date"] = pd.to_datetime(df["Date"])
        
        # Filter for future games
        today = datetime.now()
        upcoming_games = df[df["Date"] > today]
        
        # Print the next game
        if not upcoming_games.empty:
            next_game = upcoming_games.iloc[0]
            global next_game_date
            next_game_date = next_game['Date'].strftime('%Y-%m-%d')
            print(f"next game date: {next_game['Date'].strftime('%Y-%m-%d')}")
            global next_opponent
            next_opponent = next_game['Opponent']
            print(f'next opp is {next_opponent}')
        else:
            print(f"No upcoming games found for {team_abbreviation}.")
    else:
        print("Schedule table not found on the page.")
