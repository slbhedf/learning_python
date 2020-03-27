# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

left1 = 0
bottom1 = 0
width1 = 1
height1 = 1

left2 = 0
bottom2 = 1.2
width2 = 1
height2 = 1

fig = plt.figure()
ax1 = fig.add_axes([left1, bottom1, width1, height1])
ax2 = fig.add_axes([left2, bottom2, width2, height2])

ax1.plot(np.arange(0,10), np.ones(10))
ax2.plot(np.arange(0,10), np.arange(0,10))

ax1.set_title('y=1')
ax2.set_title('y=x')