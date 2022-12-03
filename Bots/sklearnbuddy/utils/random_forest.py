import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn.linear_model
import os
from plotnine import ggplot, geom_point, aes





# Import game data
games = pd.read_csv("Bots/sklearnbuddy/utils/first_50_games.csv")

games.head()

# Create new variable indicating if the requested move was played by winner
games["winner_move"] = (games["white_won"] == games["whites_turn"])

games.head()

# Is this move a winner's move or a loser's move?
# Can train separate models for white & black

whites_moves = games[(games["whites_turn"] == 1)]
blacks_moves = games[(games["whites_turn"] == 0)]

games.names()


