# -*- coding: utf-8 -*-

import pandas as pd
from datetime import timedelta, datetime
import matplotlib.pyplot as plt
import numpy as np
import os

class DateChart(object):
    def __init__(self, firstdate, enddate):
        self.fig = plt.figure(figsize=(15,15))
        self.ax = self.fig.subplots()
        self.set_firstdate(firstdate)
        self.set_enddate(enddate)
        
    def set_firstdate(self, d):
        self.firstdate = d
        
    def set_enddate(self, d):
        self.enddate = d
        
    def set_datelabels(self):
        xmajor_ticks = []
        xminor_ticks = []
        xmajor_labels = []
        xminor_labels = []
        i = 0
        d = self.firstdate
        while(d <= self.enddate):
            if d.weekday() == 6:
                xmajor_ticks.append(i)
                xmajor_labels.append(d.strftime("%b %d"))
            else:
                xminor_ticks.append(i)
                xminor_labels.append(d.strftime("%b %d"))
            d = d + timedelta(days=1)
            i += 1
        self.ax.set_xticks(xmajor_ticks, minor=False)
        self.ax.set_xticks(xminor_ticks, minor=True)
        self.ax.set_xticklabels(xmajor_labels, minor=False)
        self.ax.grid(True, which='both')
        self.ax.tick_params(which='major', length=10)
        plt.xticks(rotation=70)
        for tick in self.ax.xaxis.get_major_ticks():
            tick.label.set_fontsize(20) 

    def dates_to_x(self, dates):
        dt = dates[0] - self.firstdate
        i = dt.days
        x = np.arange(i, len(dates)+i)
        return x
    
    def set_logscale_yticks(self, maxdigits=5):
        k = 0
        ymajor_ticks = []
        yminor_ticks = []
        while(k < maxdigits):
            i = 10 ** k
            j = 1
            while(j <= 9):
                num = i*j
                if j == 1:
                    ymajor_ticks.append(num)
                else:
                    yminor_ticks.append(num)
                j += 1
            k += 1
        ymajor_labels = list(map(lambda i: "{:,d}".format(i), ymajor_ticks))
        yminor_labels = list(map(lambda i: "{:,d}".format(i), yminor_ticks))
        self.ax.set_yticks(ticks=ymajor_ticks, minor=False)
        self.ax.set_yticks(ticks=yminor_ticks, minor=True)
        self.ax.set_yticklabels(ymajor_labels, minor=False)
        self.ax.set_yticklabels(yminor_labels, minor=True)    

def covid19_worlddatechart():
    firstdate = datetime(2020,1,10)
    enddate = datetime.today() - timedelta(days=1)
    chart = DateChart(firstdate, enddate)
    chart.set_datelabels()
    chart.ax.set_yscale('log')
    chart.ax.set_ylabel('total deaths', fontsize='25')
    chart.set_logscale_yticks()
    chart.ax.set_ylim(0.90, 30000)
    for tick in chart.ax.yaxis.get_major_ticks():
        tick.label.set_fontsize(12) 

    df_all = pd.read_csv('full_data.csv', parse_dates=['date'])
    df_all = df_all.loc[lambda df: df['date'] <= enddate,:]
    
    countries = ['Italy', 'Spain','United Kingdom', 'Germany', 'France', 'United States', 'China', 'Iran']
    #countries = ['Italy', 'Spain','United Kingdom', 'Germany', 'France', 'United States', 'China', 'Japan', 'Iran', 'Netherlands', 'Belgium']
    markerlist = ['*-', 'o-', 'X-', 'D-', 'H-', 's-', 'P-', 'v-']
    markerdict = {}
    countries.sort()
    df_dict = {}
    
    for country in countries:
        df = df_all.loc[lambda df: df['location'] == country, :]
        df_dict[country] = df
        markerdict[country] = markerlist.pop()
    
    for country in df_dict.keys():
        df = df_dict[country]
        df = df.loc[lambda df: df['total_deaths'] > 0, :]
        x = chart.dates_to_x(list(df['date']))
        y = list(df['total_deaths'])
        chart.ax.plot(x, y, markerdict[country], label=country)
    
    chart.ax.legend(loc='best',prop={'size': 20}, frameon=True)
    
    try:
        os.mkdir('svg')
    except OSError:
        print("directory already exists")
        
    plt.tight_layout()
    plt.show()
    chart.fig.savefig('svg/deaths_caused_by_coronavirus.svg')    

def covid19_japanese_pref_datechart():
    pass

if __name__ == '__main__':
    covid19_worlddatechart()
    