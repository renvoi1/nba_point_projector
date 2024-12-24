import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

#load json file
loaded_df = pd.read_json("player_stats.json", orient="records")
print(loaded_df)

# Example DataFrame
# Ensure you have a DataFrame `df` with player stats
# Features: Columns with stats like FG, REB, AST, MIN, etc.
# Target: Points scored (e.g., 'PTS')

# df = ... # Load or create your dataset here
features = ["PPG", "MPG", "FGA", "NXTOPP", "NXTGM", "OPPDR", "OPPDREB", "LSTGM", "DATEDIFF", "B2B", "ISGMAWAY"]
target = "PTS"

# Ensure no missing data
df = loaded_df.dropna(subset=features + [target])

# Split into features (X) and target (y)
X = df[features]
y = df[target]

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# WIP, I HAVE NO IDEA HOW MACHINE LEARNING WORKS SO IM GOING TO PROCRASTINATE THIS PART