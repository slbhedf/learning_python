# -*- coding: utf-8 -*-

import pandas as pd
from datetime import timedelta, datetime
import matplotlib.pyplot as plt
import numpy as np
import os

class DateChart(object):
    def __init__(self):
        self.fig = plt.figure(figsize=(15,15))
        self.ax = self.fig.subplots()
        
    def set_startdate(self, d):
        self.startdate = d
        
    def set_enddate(self, d):
        self.enddate = d
        
    def set_datelabels(self):
        xmajor_ticks = []
        xminor_ticks = []
        xmajor_labels = []
        i = 0
        d = self.startdate
        while(d <= self.enddate):
            if d.weekday() == 6:
                xmajor_ticks.append(i)
                xmajor_labels.append(d.strftime("%b %d"))
            else:
                xminor_ticks.append(i)
            d = d + timedelta(days=1)
            i += 1
        self.ax.set_xticks(xmajor_ticks, minor=False)
        self.ax.set_xticks(xminor_ticks, minor=True)
        self.ax.set_xticklabels(xmajor_labels)
        self.ax.grid(True, which='both')
        self.ax.tick_params(which='major', length=10)
        plt.xticks(rotation=70)
        for tick in self.ax.xaxis.get_major_ticks():
            tick.label.set_fontsize(20) 

    def dates_to_x(self, dates):
        deltatime = dates[0] - self.startdate
        i = deltatime.days
        x = np.arange(i, len(dates)+i)
        return x
    
    def set_logscale_yticks(self, maxnum=20000):
        k = 0
        ymajor_ticks = []
        yminor_ticks = []
        while(True):
            i = 10 ** k
            j = 1
            num = i*j
            if num >= maxnum:
                    break
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
        self.ax.set_yticklabels(ymajor_labels)
        self.ax.set_yticklabels(yminor_labels, minor=True)    



if __name__ == '__main__':
    yesterday = datetime.today() - timedelta(days=1)
    startdate = datetime(2020,1,10)
    chart = DateChart()
    chart.set_startdate(startdate)
    chart.set_enddate(yesterday)
    chart.set_datelabels()
    chart.ax.set_yscale('log')
    chart.ax.set_ylabel('total deaths', fontsize='25')
    chart.set_logscale_yticks()
    chart.ax.set_ylim(0.90, 50000)
    for tick in chart.ax.yaxis.get_major_ticks():
        tick.label.set_fontsize(12) 

    df_all = pd.read_csv('full_data.csv', parse_dates=['date'])
    df_all = df_all.loc[lambda df: df['date'] <= yesterday,:]
    
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
    chart.fig.savefig('svg/deaths_caused_by_coronavirus.svg')    
