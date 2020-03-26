# -*- coding: utf-8 -*-

from matplotlib import pyplot as plt
import numpy as np

x = np.arange(0,2*np.pi, 0.05)
y = np.cos(x)
fig, ax = plt.subplots()  
ax.plot(x, y)  

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('y=cos(x)')

fig.set_size_inches(10, 10) 

ax.grid(axis='both')

xaxis_ticks=[np.pi/6.0, np.pi/4.0, np.pi/3.0, np.pi/2.0]
xlabels = ['pi/6', 'pi/4' , 'pi/3' ,'pi/2']
plt.xticks(ticks=xaxis_ticks, labels=xlabels, rotation=30)

plt.show()

