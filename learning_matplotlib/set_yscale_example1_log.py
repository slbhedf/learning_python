# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

def set_yscale_log_example_polynomial1():    
    fig = plt.figure()
    ax = fig.subplots()
    x = np.arange(0.1, 10, 0.05)
    ylist = []
    ylist.append({'array':x, 'label': 'y=x' }) 
    ylist.append({'array': x * x, 'label': 'y=x*x'})
    ylist.append({'array': x ** 3, 'label': 'y=x*x*x'})
    
    for y in ylist:
        ax.plot(x, y['array'], label=y['label'])
        
    ax.set_title('xaxis scale is linear, yaxis scale is log')
    
    ax.set_xscale('linear')
    ax.set_xlabel('linear scale')
    ax.set_yscale('log')
    ax.set_ylabel('log scale')
    
    ax.legend()
    fig.savefig('set_yscale_log_example_p1.svg')
    plt.show()

def set_yscale_log_example_polynomial2():
    fig = plt.figure()
    ax = fig.subplots()
    x = np.arange(0.1, 10, 0.05)
    ylist = []
    ylist.append({'array':x, 'label': 'y=x' }) 
    ylist.append({'array': x * x, 'label': 'y=x*x'})
    ylist.append({'array': x ** 3, 'label': 'y=x*x*x'})
    
    for y in ylist:
        ax.plot(x, y['array'], label=y['label'])
        
    ax.set_title('both axes scale are log')

    ax.set_xscale('log')
    ax.set_xlabel('log scale')
    ax.set_yscale('log')
    ax.set_ylabel('log scale')

    ax.legend()    
    fig.savefig('set_yscale_log_example_p2.svg')
    plt.show()

def set_yscale_log_example_exponential1():
    fig = plt.figure()
    ax = fig.subplots()
    x = np.arange(0.1, 10, 0.05)
    ylist = []
    ylist.append({'array': np.exp2(x), 'label': 'y=2^x' })
    ylist.append({'array': np.exp(x), 'label': 'y=e^x'})
    
    for y in ylist:
        ax.plot(x, y['array'], label=y['label'])
    
    ax.set_title('xaxis scale is linear, yaxis scale is log')

    ax.set_xscale('linear')
    ax.set_xlabel('linear scale')
    ax.set_yscale('log')
    ax.set_ylabel('log scale')
        
    ax.legend()    
    fig.savefig('set_yscale_log_example_e1.svg')
    plt.show()

def set_yscale_log_example_exponential2():
    fig = plt.figure()
    ax = fig.subplots()
    x = np.arange(0.1, 10, 0.05)
    ylist = []
    ylist.append({'array': np.exp2(x), 'label': 'y=2^x' })
    ylist.append({'array': np.exp(x), 'label': 'y=e^x'})
    
    for y in ylist:
        ax.plot(x, y['array'], label=y['label'])
    
    ax.set_title('both axes scale are log')

    ax.set_xscale('log')
    ax.set_xlabel('log scale')
    ax.set_yscale('log')
    ax.set_ylabel('log scale')
        
    ax.legend()   
    fig.savefig('set_yscale_log_example_e2.svg')
    plt.show()
    
if __name__ == '__main__':
    set_yscale_log_example_polynomial1()
    set_yscale_log_example_polynomial2()
    set_yscale_log_example_exponential1()
    set_yscale_log_example_exponential2()
    
    