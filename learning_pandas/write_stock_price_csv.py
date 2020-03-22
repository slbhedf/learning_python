# -*- coding: utf-8 -*-

import pandas as pd

path = 'HistoricalPrices.csv' # download from https://www.wsj.com/market-data/quotes/index/DJIA/historical-prices
sep = ', '
data = pd.read_csv(path, header=0, sep=sep, parse_dates=['Date'], engine='python')
df = pd.DataFrame(data)
df = df.sort_values(by=['Date'])

percents_list = []
changes_list =[]
yesterday = 0
today = 0
isfirstloop = True

for i in df.index:
    yesterday = today
    today = df['Close'][i]
    
    if isfirstloop:
        changes_list.append(float('nan'))
        percents_list.append(float('nan'))
        isfirstloop=False
        continue
    
    change = today - yesterday
    percent = 100*change/yesterday
    
    changes_list.append(round(change,2))
    percents_list.append(round(percent,2))

df['Changes'] = pd.Series(changes_list, index=df.index)
df['Percents'] = pd.Series(percents_list, index=df.index)

df.to_csv('table.csv', index=False)
