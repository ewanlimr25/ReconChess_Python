import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn.linear_model
import os
from plotnine import ggplot, geom_point, aes

# Import game data
games = pd.read_csv("first_50_games.csv")

# Create new variable indicating if the requested move was played by winner
games["winner_move"] = (games["white_won"] == games["whites_turn"])

# Just examine the winner move-related columns
games.loc[:, "white_won":"winner_move"]


games["requested_move"].unique().size

# white's losers
whites_losers = games[(games["winner_move"] == 0) &
                      (games["whites_turn"] == 1)]

# black's losers
blacks_losers = games[(games["winner_move"] == 0) &
                      (games["whites_turn"] == 0)]

# white's winners
whites_winners = games[(games["winner_move"] == 1) &
                       (games["whites_turn"] == 1)]

# black's winners
blacks_winners = games[(games["winner_move"] == 1) &
                       (games["whites_turn"] == 0)]

whites_losers_counts = whites_losers['requested_move'].value_counts()
whites_winners_counts = whites_winners['requested_move'].value_counts()
blacks_losers_counts = blacks_losers['requested_move'].value_counts()
blacks_winners_counts = games['requested_move'].value_counts()


print(count)


count = df['A'].value_counts()
print(count)

print(type(games))

X = np.c_[games["a1P"]]
y = np.c_[games["requested_move"]]

games.plot(kind='scatter', x='a1P', y='requested_move')
plt.show()

 

from plotnine import ggplot, geom_point, aes, stat_smooth, facet_wrap
from plotnine.data import mtcars

(ggplot(mtcars, aes('wt', 'mpg', color='factor(gear)'))
 + geom_point()
 + stat_smooth(method='lm')
 + facet_wrap('~gear'))
