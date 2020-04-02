# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
x = np.linspace(0, 10*np.pi, 1000)
ax.plot(x, np.cos(x))

xticks = []
xtickslabels = []

for i in range(11):
    xticks.append(i*np.pi)
    xtickslabels.append(str(i)+"π")
    
ax.set_xticks(xticks)
ax.set_xticklabels(xtickslabels)

plt.show()