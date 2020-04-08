# -*- coding: utf-8 -*-

import pandas as pd
from datetime import timedelta, datetime
import matplotlib.pyplot as plt

def set_datelabels(start, end, ax):
    xticks = []
    xlabels = []
    i = 0
    d = start
    while(d <= end):
        xticks.append(i)
        xlabels.append(d.isoformat()[:10])
        d = d + timedelta(days=1)
        i += 1
    ax.set_xticks(ticks=xticks)
    ax.set_xticklabels(xlabels)
    ax.grid(True)
    plt.xticks(rotation=70)

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
fig = plt.figure(figsize=(20,20))
ax = fig.subplots()
set_datelabels(datetime(2020,2,10), datetime(2020,4,8), ax)
ax.set_yscale('log')
set_logscale_yticks(ax)
ax.set_ylim(0.90, 20000)
#ax.set_xlim()

df_all = pd.read_csv('full_data.csv', parse_dates=['date'])

countries = ['Italy', 'Spain','United Kingdom', 'Germany', 'France', 'United States']
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

ax.legend()

fig.savefig('deaths_caused_by_coronavirus.svg')    
