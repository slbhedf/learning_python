# -*- coding: utf-8 -*-
# https://matplotlib.org/3.2.1/api/_as_gen/matplotlib.pyplot.subplot.html

import matplotlib.pyplot as plt
import numpy as np

ax1 = plt.subplot(2,2,1) 
ax2 = plt.subplot(2,2,2)
ax3 = plt.subplot(2,2,3)
ax4 = plt.subplot(2,2,4)

x = np.arange(0, 10, 0.05)

y1 = x
ax1.plot(x, y1)
ax1.grid(True)

y2 = np.sqrt(x)
ax2.plot(x, y2)
ax2.grid(ls='-.')

y3 = x * x
ax3.plot(x, y3)
ax3.grid(ls='-')

y4 = np.exp2(x)
ax4.plot(x, y4)
ax4.grid(ls='-')


plt.show()