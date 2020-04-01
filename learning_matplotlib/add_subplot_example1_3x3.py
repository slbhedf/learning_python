# -*- coding: utf-8 -*-
# https://matplotlib.org/3.2.1/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure.add_subplot

import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(10,10))

ax1 = fig.add_subplot(3,3,1) 
ax2 = fig.add_subplot(3,3,2)
ax3 = fig.add_subplot(3,3,3)

ax4 = fig.add_subplot(334)
ax5 = fig.add_subplot(335)
ax6 = fig.add_subplot(336)

ax7 = fig.add_subplot(3,3,7)
ax8 = fig.add_subplot(3,3,8)
ax9 = fig.add_subplot(3,3,9)

x = np.arange(0, 30, 0.05)

y1 = x
ax1.plot(x, y1)
ax1.grid(True)
ax1.set_title('y=x')

y2 = x * x
ax2.plot(x, y2)
ax2.grid(True)
ax2.set_title('y=x*x')

y3 = x ** 3
ax3.plot(x, y3)
ax3.grid(True)
ax3.set_title('y=x*x*x')

y4 = np.sin(x)
ax4.plot(x, y4)
ax4.grid(True)
ax4.set_title('y=sin(x)')

y5 = np.sin(2*x)
ax5.plot(x, y5)
ax5.grid(True)
ax5.set_title('y=sin(2*x)')

y6 = np.sin(3*x)
ax6.plot(x, y6)
ax6.grid(True)
ax6.set_title('y=sin(3*x)')

y7 = x + np.cos(x)
ax7.plot(x, y7)
ax7.grid(True)
ax7.set_title('y=x+cos(x)')

y8 = x + np.cos(2*x)
ax8.plot(x, y8)
ax8.grid(True)
ax8.set_title('y=x+cos(2*x)')

y9 = x + np.cos(3*x)
ax9.plot(x, y9)
ax9.grid(True)
ax9.set_title('y=x+cos(3*x)')

plt.tight_layout()
fig.savefig('subplot_example1_3x3.svg')
plt.show()
