from nba_api.stats.endpoints import playergamelog
from nba_api.stats.static import players
import pandas as pd



# This program was proof of concept to see how nba_api functioned, this file is not important for the overall project.


# get player details (name)
all_players = players.get_players()
while True:
    try:
        asked_player = input("Please input player (case sens): ")
        player = [player for player in all_players if player['full_name'] == asked_player][0]
        break
    except IndexError:
        print('player does not exist/wrong case')
player_id = player['id']

# get game log from specified season from player
season = input("Plese input season (20XX-XX): ")
gamelog = playergamelog.PlayerGameLog(player_id=player_id, season=season)

# conv to pandas df
df_gamelog = gamelog.get_data_frames()[0]

# converting dtype and prevent throwing future warning
df_gamelog1 = df_gamelog.convert_dtypes()
with pd.option_context("future.no_silent_downcasting", True):
    df_gamelog2 = df_gamelog1.fillna(0)

# print(df_gamelog2)

# calc avg ppg, apg, rpg, pl/ms
if not df_gamelog2.empty:
    avg_points_per_game = df_gamelog2['PTS'].mean()
    avg_ast_per_game = df_gamelog2['AST'].mean()
    avg_reb_per_game = df_gamelog2['REB'].mean()
    avg_plus_minus = df_gamelog2['PLUS_MINUS'].mean()
    print(f"Average points per game for {player['full_name']} in the {season} season: {avg_points_per_game:.2f}")
    print(f"Average assists per game for {player['full_name']} in the {season} season: {avg_ast_per_game:.2f}")
    print(f"Average rebounds per game for {player['full_name']} in the {season} season: {avg_reb_per_game:.2f}")
    if avg_plus_minus == (0):
        print("pl/ms was not calculated at this time")
    else:
        print(f"Average Plus/Minus per game for {player['full_name']} in the {season} season {avg_plus_minus}")
else:
    print(f"No game log data found for season {season}.")
