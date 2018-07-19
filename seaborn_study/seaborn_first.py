#! /bin/env python

print('hello seaborn')

import pandas as pd
import numpy as np

from matplotlib import pyplot as plt

import seaborn as sns

df = pd.read_csv('Pokemon.csv',index_col=0)

df.head()

#sns.lmplot(x = 'Attack', y = 'Defense', data = df)


sns.set_style("whitegrid")
plt.plot(np.arange(10))
plt.show()
