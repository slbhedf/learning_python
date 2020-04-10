# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

def set_yscale_log_example():
    nrow = 2
    ncol = 3
    width = 18
    height = 12
    fig = plt.figure(figsize=(width, height))
    ax = fig.subplots(nrow, ncol)
    x = np.arange(0.1, 10, 0.05)
    
    polynomials = []
    polynomials.append({'array':x, 'label': 'y=x' }) 
    polynomials.append({'array': x * x, 'label': 'y=x*x'})
    polynomials.append({'array': x ** 3, 'label': 'y=x*x*x'})
    
    exponentials = []
    exponentials.append({'array': np.exp2(x), 'label': 'y=2^x' })
    exponentials.append({'array': np.exp(x), 'label': 'y=e^x'})
    
    imax = ax.shape[0]
    jmax = ax.shape[1]
    for i in range(imax):
        for j in range(jmax):
            
            if i == 0:
                # plot 3 polynomial functions
                for y in polynomials:
                    ax[i][j].plot(x, y['array'], label=y['label']) 
            else:
                # plot 3 exponential functions
                for y in exponentials:
                    ax[i][j].plot(x, y['array'], label=y['label'])
                    
            if j == 0:
                # both axes scale are linear
                ax[i][j].set_title('both axes scales are linear') 
                # xaxis scale is linear
                ax[i][j].set_xscale('linear')
                ax[i][j].set_xlabel('linear scale')
                # yaxis scale is linear
                ax[i][j].set_yscale('linear')
                ax[i][j].set_ylabel('linear scale')
            elif j == 1:
                # xaxis scale is linear, yaxis scale is log
                ax[i][j].set_title('xaxis scale is linear, yaxis scale is log')
                # xaxis scale is linear
                ax[i][j].set_xscale('linear')
                ax[i][j].set_xlabel('linear scale')
                # yaxis scale is log
                ax[i][j].set_yscale('log')
                ax[i][j].set_ylabel('log scale')
            else:
                # both axes scale are log
                ax[i][j].set_title('both axes scales are log')
                # xaxis scale is log
                ax[i][j].set_xscale('log')
                ax[i][j].set_xlabel('log scale')
                # yaxis scale is log
                ax[i][j].set_yscale('log')
                ax[i][j].set_ylabel('log scale')
                
            ax[i][j].legend()
    fig.savefig('set_yscale_log_example1_2x2.svg')
    plt.tight_layout()
    plt.show()
      
if __name__ == '__main__':
    set_yscale_log_example()
