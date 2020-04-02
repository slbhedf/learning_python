# -*- coding: utf-8 -*-
# https://matplotlib.org/3.2.1/api/_as_gen/matplotlib.pyplot.subplot.html

import matplotlib.pyplot as plt
import numpy as np
import random

fig, ax = plt.subplots(3,3, figsize=(10,10))

x = np.arange(0, 10, 0.05)
ylist = [x , np.sqrt(x), x ** 2, np.sin(x), np.cos(x), np.exp(x), np.exp2(x) ] 
colors = ['b','g','r','b','c','m','y','k','b','w']
linestyles = ['-', '--', '-.', ':']

for i in range(ax.shape[0]):
    for j in range(ax.shape[1]):
        y = random.choice(ylist)
        linewidth = random.randint(5, 10) * 0.1 # 0.5-1.0
        linestyle = random.choice(linestyles)
        gridcolor = random.choice(colors)
        
        ax[i][j].plot(x, y)
        ax[i][j].grid(color=gridcolor, ls=linestyle, lw=linewidth)

fig.tight_layout()
plt.show()