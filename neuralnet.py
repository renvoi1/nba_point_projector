import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

#load json file
loaded_df = pd.read_json("player_stats.json", orient="records")
print(loaded_df)