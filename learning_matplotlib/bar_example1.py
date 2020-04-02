# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
from string import ascii_lowercase

fig, ax = plt.subplots(figsize=(10,10))

alphabet = list(ascii_lowercase)
numbers = np.arange(1,len(alphabet)+1)
height = list(map(lambda x: 1.2**x, numbers))

ax.bar(alphabet, height)
ax.plot(height, 'r')

fig.savefig('bar_graph_a2z.svg')
