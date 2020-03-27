# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

nrows = 2
ncols = 3
fig, axes = plt.subplots(nrows, ncols, figsize = (12,8))
x = np.arange(0, 2*np.pi, 0.05)

axes[0][0].plot(x, np.cos(x), 'g',lw=6) # linecolor=green, linewidth=6
axes[0][0].grid(True)
axes[0][0].set_title('y=cos(x)')

axes[0][1].plot(x, np.cos(2*x), 'r', lw=5)
axes[0][1].grid(color='k', ls = '-', lw = 0.25)
axes[0][1].set_title('y=cos(2x)')

axes[0][2].plot(x, np.cos(3*x), lw=4)
axes[0][2].grid(color='b', ls='-', lw=1)
axes[0][2].set_title('y=cos(3x)')

axes[1][0].plot(x, np.cos(4*x), 'g', lw=3)
axes[1][0].grid(color='c', ls='--')
axes[1][0].set_title('y=cos(4x)')

axes[1][1].plot(x, np.cos(5*x), 'r--', lw=2)
axes[1][1].grid(color='g', ls = '--', lw = 0.5)
axes[1][1].set_title('y=cos(5x)')

axes[1][2].plot(x, np.cos(6*x), lw=1)
axes[1][2].set_title('y=cos(6x)')

fig.tight_layout()
plt.savefig('six_cosines.svg')
plt.show()


