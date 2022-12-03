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

# white's games

whites_losers_counts = whites_losers['requested_move'].value_counts()

whites_winners_counts = whites_winners['requested_move'].value_counts()

blacks_losers_counts = blacks_losers['requested_move'].value_counts()

blacks_winners_counts = games['requested_move'].value_counts()


def return_counts(series, win):
    df = pd.DataFrame(series)
    df.index.name = 'move'
    df.reset_index(inplace=True)
    if win:
        df = df.rename({'requested_move': 'win_count'}, axis=1)
    else:
        df = df.rename({'requested_move': 'loss_count'}, axis=1)
    return (df)


white_lose = return_counts(whites_losers_counts, win=False)
white_win = return_counts(whites_winners_counts, win=True)
black_lose = return_counts(blacks_losers_counts, win=False)
black_win = return_counts(blacks_winners_counts, win=True)

white_moves = white_win.merge(white_lose, on='move')

no_skip = white_moves[white_moves['move'] != 'skip']

no_skip

X = no_skip['win_count']
Y = no_skip['loss_count']

a = list(no_skip['move'])


plt.figure(figsize=(8, 6))
plt.scatter(X, Y, s=100, color="red")
plt.xlabel("X")
plt.ylabel("Y")
for i, label in enumerate(a):
    plt.annotate(label, (X[i], Y[i]))
plt.show()

plt.show()


no_skip.plot(kind='scatter', x='win_count', y='loss_count')
plt.show()

x = no_skip['win_count']
y = no_skip['loss_count']
jittered_y = y + 0.5 * np.random.rand(len(y)) - 0.05
jittered_x = x + 0.5 * np.random.rand(len(x)) - 0.05
plt.figure(figsize=(10,5))
plt.scatter(jittered_x,jittered_y,s=10,alpha=0.5)

for i, txt in enumerate(x):
    plt.annotate(txt, (x[i], y[i]))

plt.title('Y and X Jittered')
plt.show()

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


plt.scatter(x, y)

for i, txt in enumerate(x):
    print(type(i))
    print(x[i])

x[4]
