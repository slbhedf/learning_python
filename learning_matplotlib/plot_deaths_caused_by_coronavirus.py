# -*- coding: utf-8 -*-

import pandas as pd
from datetime import timedelta, datetime
import matplotlib.pyplot as plt

def set_datelabels(start, end, ax):
    xmajor_ticks = []
    xminor_ticks = []
    xlabels = []
    i = 0
    d = start
    while(d <= end):
        if i % 7 == 0:
            xmajor_ticks.append(i)
            xlabels.append(d.isoformat()[:10])
        else:
            xminor_ticks.append(i)
            
        d = d + timedelta(days=1)
        i += 1
        
    ax.set_xticks(xmajor_ticks, minor=False)
    ax.set_xticks(xminor_ticks, minor=True)
    ax.set_xticklabels(xlabels)
    
    ax.grid(True, which='both')
    ax.tick_params(which='major', length=10)
    plt.xticks(rotation=70)

    for tick in ax.xaxis.get_major_ticks():
        tick.label.set_fontsize(20) 

def dates_to_ints(dates, ax):
    date_string = ax.get_xticklabels()[0].get_text()
    start = datetime.fromisoformat(date_string)
    i = (dates[0] - start).days
    x = []
    d = dates[0]
    while(d <= dates[-1]):
        x.append(i)
        i += 1
        d += timedelta(days=1)
    return x

def set_logscale_yticks(ax):
    yticks = []
    k = 0
    while(k <= 5):
        i = 10 ** k
        j = 1
        while(j <= 9):
            yticks.append(i*j)
            j +=1
        k += 1
    yticklabels = list(map(lambda i: "{:,d}".format(i), yticks))
    ax.set_yticks(ticks=yticks)
    ax.set_yticklabels(yticklabels)

################## 
fig = plt.figure(figsize=(25, 25))
ax = fig.subplots()
set_datelabels(datetime(2020,1,10), datetime(2020,4,7), ax)
ax.set_yscale('log')
ax.set_ylabel('total deaths', fontsize='20')
set_logscale_yticks(ax)
ax.set_ylim(0.90, 20000)

for tick in ax.yaxis.get_major_ticks():
    tick.label.set_fontsize(20) 

df_all = pd.read_csv('full_data.csv', parse_dates=['date'])

countries = ['Italy', 'Spain','United Kingdom', 'Germany', 'France', 'United States', 'China', 'Iran']
#countries = ['Italy', 'Spain','United Kingdom', 'Germany', 'France', 'United States', 'China', 'Japan', 'Iran', 'Netherlands', 'Belgium']
countries.sort()
df_dict = {}

for country in countries:
    df = df_all.loc[lambda df: df['location'] == country, :]
    df_dict[country] = df

for country in df_dict.keys():
    df = df_dict[country]
    df = df.loc[lambda df: df['total_deaths'] > 0, :]
    x = dates_to_ints(list(df['date']), ax)
    y = list(df['total_deaths'])
    ax.plot(x, y, label=country)

ax.legend(loc='best',prop={'size': 30}, frameon=True)

fig.savefig('deaths_caused_by_coronavirus.svg')    
