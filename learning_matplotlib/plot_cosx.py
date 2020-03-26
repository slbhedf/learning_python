# -*- coding: utf-8 -*-

from matplotlib import pyplot as plt
import numpy as np

x = np.arange(0, np.pi, 0.05)
y = np.cos(x)
fig, ax = plt.subplots()  
ax.plot(x, y)  

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('y=cos(x)')

fig.set_size_inches(10, 10) 

ax.grid(axis='both')

xaxis_ticks=[0, np.pi/6.0, np.pi/4.0, np.pi/3.0, np.pi/2.0, 2*np.pi/3.0, 3*np.pi/4.0, 5*np.pi/6.0, np.pi]
xlabels = ['0', 'π/6', 'π/4' , 'π/3' ,'π/2', '2π/3', '3π/4', '5π/6', 'π']
plt.xticks(ticks=xaxis_ticks, labels=xlabels, rotation=30)

yaxis_ticks=list(map(np.cos, xaxis_ticks))
ylabels = ['1','√3/2', '√2/2', '1/2', '0', '-1/2', '-√2/2', '-√3/2', '-1']
plt.yticks(ticks=yaxis_ticks, labels=ylabels, rotation=0)

plt.savefig('cosx_20200326.svg')

plt.show()

