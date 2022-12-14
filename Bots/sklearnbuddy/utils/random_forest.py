import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn.linear_model
import os
from plotnine import ggplot, geom_point, aes

#|%%--%%| <AvLKKyGCMI|dS1ABHMUkw>

# Import game data
games = pd.read_csv("Bots/sklearnbuddy/utils/first_50_games.csv")

games.head()

# Create new variable indicating if the requested move was played by winner
games["winner_move"] = (games["white_won"] == games["whites_turn"])

# Create new variables separating out the requested move into numbers
req_moves = pd.DataFrame(games["requested_move"])

req_moves["start_file"] = req_moves["requested_move"].map(lambda a: a[0:1])
req_moves["start_rank"] = req_moves["requested_move"].map(lambda a: a[1:2])
req_moves["end_file"] = req_moves["requested_move"].map(lambda a: a[2:3])
req_moves["end_rank"] = req_moves["requested_move"].map(lambda a: a[3:4])

# https://stackoverflow.com/a/34348352
req_moves["start_file_a"] = 0
req_moves.loc[req_moves["start_file"] == "a", "start_file_a"] = 1
req_moves["start_file_b"] = 0
req_moves.loc[req_moves["start_file"] == "b", "start_file_b"] = 1
req_moves["start_file_c"] = 0
req_moves.loc[req_moves["start_file"] == "c", "start_file_c"] = 1
req_moves["start_file_d"] = 0
req_moves.loc[req_moves["start_file"] == "d", "start_file_d"] = 1
req_moves["start_file_e"] = 0
req_moves.loc[req_moves["start_file"] == "e", "start_file_e"] = 1
req_moves["start_file_f"] = 0
req_moves.loc[req_moves["start_file"] == "f", "start_file_f"] = 1
req_moves["start_file_g"] = 0
req_moves.loc[req_moves["start_file"] == "g", "start_file_g"] = 1

req_moves["start_rank_1"] = 0
req_moves.loc[req_moves["start_rank"] == "1", "start_rank_1"] = 1
req_moves["start_rank_2"] = 0
req_moves.loc[req_moves["start_rank"] == "2", "start_rank_2"] = 1
req_moves["start_rank_3"] = 0
req_moves.loc[req_moves["start_rank"] == "3", "start_rank_3"] = 1
req_moves["start_rank_4"] = 0
req_moves.loc[req_moves["start_rank"] == "4", "start_rank_4"] = 1
req_moves["start_rank_5"] = 0
req_moves.loc[req_moves["start_rank"] == "5", "start_rank_5"] = 1
req_moves["start_rank_6"] = 0
req_moves.loc[req_moves["start_rank"] == "6", "start_rank_6"] = 1
req_moves["start_rank_7"] = 0
req_moves.loc[req_moves["start_rank"] == "7", "start_rank_7"] = 1

req_moves["end_file_a"] = 0
req_moves.loc[req_moves["end_file"] == "a", "end_file_a"] = 1
req_moves["end_file_b"] = 0
req_moves.loc[req_moves["end_file"] == "b", "end_file_b"] = 1
req_moves["end_file_c"] = 0
req_moves.loc[req_moves["end_file"] == "c", "end_file_c"] = 1
req_moves["end_file_d"] = 0
req_moves.loc[req_moves["end_file"] == "d", "end_file_d"] = 1
req_moves["end_file_e"] = 0
req_moves.loc[req_moves["end_file"] == "e", "end_file_e"] = 1
req_moves["end_file_f"] = 0
req_moves.loc[req_moves["end_file"] == "f", "end_file_f"] = 1
req_moves["end_file_g"] = 0
req_moves.loc[req_moves["end_file"] == "g", "end_file_g"] = 1

req_moves["end_rank_1"] = 0
req_moves.loc[req_moves["end_rank"] == "1", "end_rank_1"] = 1
req_moves["end_rank_2"] = 0
req_moves.loc[req_moves["end_rank"] == "2", "end_rank_2"] = 1
req_moves["end_rank_3"] = 0
req_moves.loc[req_moves["end_rank"] == "3", "end_rank_3"] = 1
req_moves["end_rank_4"] = 0
req_moves.loc[req_moves["end_rank"] == "4", "end_rank_4"] = 1
req_moves["end_rank_5"] = 0
req_moves.loc[req_moves["end_rank"] == "5", "end_rank_5"] = 1
req_moves["end_rank_6"] = 0
req_moves.loc[req_moves["end_rank"] == "6", "end_rank_6"] = 1
req_moves["end_rank_7"] = 0
req_moves.loc[req_moves["end_rank"] == "7", "end_rank_7"] = 1

req_moves.iloc[1, :]



req_moves

int("05")

games.head()

# Is this move a winner's move or a loser's move?
# Can train separate models for white & black

whites_moves = games[(games["whites_turn"] == 1)]
blacks_moves = games[(games["whites_turn"] == 0)]

games.keys()

#|%%--%%| <dS1ABHMUkw|ALBd4YzEy1>
r"""°°°
The goal is to predict if a move is a winning or losing move
°°°"""
