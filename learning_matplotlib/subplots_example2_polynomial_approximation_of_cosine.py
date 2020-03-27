# -*- coding: utf-8 -*-
'''
Polynomial Approximation of cos(x) (degree=0,2,4,...,16) using Taylor Series.

This is an example of subplots().
'''

import matplotlib.pyplot as plt
import numpy as np

fig, axes = plt.subplots(3, 3, figsize = (12,12))
x = np.arange(0, 2*np.pi, 0.05)

y0 = np.ones(x.size)
axes[0][0].plot(x, np.cos(x), 'c--') # linecolor=green, linewidth=6
axes[0][0].plot(x, y0)
axes[0][0].grid(True)
axes[0][0].set_title('polynomial approximation(degree=0)')

y1 = y0 - (x**2)/2 
axes[0][1].plot(x, np.cos(x), 'c--')
axes[0][1].plot(x, y1)
axes[0][1].grid(True)
axes[0][1].set_title('polynomial approximation(degree=2)')
axes[0][1].set_ylim(-1.25, 1.25)

y2 = y1 + (x**4)/(4*3*2) 
axes[0][2].plot(x, np.cos(x), 'c--')
axes[0][2].plot(x, y2)
axes[0][2].grid(True)
axes[0][2].set_title('polynomial approximation(degree=4)')
axes[0][2].set_ylim(-1.25, 1.25)

y3 = y2 - (x**6)/(6*5*4*3*2)
axes[1][0].plot(x, np.cos(x), 'c--')
axes[1][0].plot(x, y3)
axes[1][0].grid(True)
axes[1][0].set_title('polynomial approximation(degree=6)')
axes[1][0].set_ylim(-1.25, 1.25)

y4 = y3 + (x**8)/(8*7*6*5*4*3*2)
axes[1][1].plot(x, np.cos(x), 'c--')
axes[1][1].plot(x, y4)
axes[1][1].grid(True)
axes[1][1].set_title('polynomial approximation(degree=8)')
axes[1][1].set_ylim(-1.25, 1.25)

y5 = y4 - (x**10)/(10*9*8*7*6*5*4*3*2)
axes[1][2].plot(x, np.cos(x), 'c--')
axes[1][2].grid(True)
axes[1][2].plot(x, y5)
axes[1][2].set_title('polynomial approximation(degree=10)')
axes[1][2].set_ylim(-1.25, 1.25)

y6 =  y5 + (x**12)/(12*11*10*9*8*7*6*5*4*3*2)
axes[2][0].plot(x, np.cos(x), 'c--')
axes[2][0].plot(x, y6)
axes[2][0].grid(True)
axes[2][0].set_title('polynomial approximation(degree=12)')
axes[2][0].set_ylim(-1.25, 1.25)

y7 = y6 - (x**14)/(14*13*12*11*10*9*8*7*6*5*4*3*2)
axes[2][1].plot(x, np.cos(x), 'c--')
axes[2][1].plot(x, y7)
axes[2][1].grid(True)
axes[2][1].set_title('polynomial approximation(degree=14)')
axes[2][1].set_ylim(-1.25, 1.25)

y8 = y7 + (x**16)/(16*15*14*13*12*11*10*9*8*7*6*5*4*3*2)
axes[2][2].plot(x, np.cos(x), 'c--')
axes[2][2].plot(x, y8)
axes[2][2].grid(True)
axes[2][2].set_title('polynomial approximation(degree=16)')
axes[2][2].set_ylim(-1.25, 1.25)

fig.tight_layout()
plt.savefig('polynomial_approximation_of_cosine.svg')
plt.show()


