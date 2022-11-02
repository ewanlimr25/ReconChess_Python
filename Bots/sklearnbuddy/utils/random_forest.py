import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn.linear_model
import os
from plotnine import ggplot, geom_point, aes

games = pd.read_csv("first_50_games.csv")

print(games)

print(type(games))

X = np.c_[games["a1P"]]
y = np.c_[games["requested_move"]]

games.plot(kind='scatter', x='a1P', y='requested_move')
plt.show()

(ggplot(games, aes(x='a1P', y='requested_move'))
 + geom_point()
 

from plotnine import ggplot, geom_point, aes, stat_smooth, facet_wrap
from plotnine.data import mtcars

(ggplot(mtcars, aes('wt', 'mpg', color='factor(gear)'))
 + geom_point()
 + stat_smooth(method='lm')
 + facet_wrap('~gear'))
