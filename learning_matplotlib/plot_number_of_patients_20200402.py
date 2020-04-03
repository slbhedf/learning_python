import pandas as pd
from datetime import timedelta
import matplotlib.pyplot as plt
import numpy as np

'''
plot the number of coronavirus patients in tokyo.

download the csvfile
https://catalog.data.metro.tokyo.lg.jp/dataset/t000010d0000000068

I also predit the number of patients in a bad cases until 2020-04-16.
'''

name = '130001_tokyo_covid19_patients.csv'
data = pd.read_csv(name, parse_dates=['公表_年月日'])
df = pd.DataFrame(data, columns=['都道府県名', '公表_年月日'])
df = df.loc[lambda df: df['都道府県名'] == '東京都',:]
df = df.sort_values(by=['公表_年月日'], ascending=True)

dict = {}

for i in df.index:
    if pd.isnull(df['公表_年月日'][i]):
        continue
    if dict.get(df['公表_年月日'][i]):
        dict[df['公表_年月日'][i]] += 1
    else:
        dict[df['公表_年月日'][i]] = 1

date_list = list(dict.keys())
date_list.sort()

d = date_list[0]
x = []
y = []
n = 0
while(d <= date_list[len(date_list)-1]):
    n += dict.get(d, 0)
    x.append(d.isoformat()[:10])
    y.append(n)
    d = d + timedelta(days=1)
    
#print(x)
#print(y)

fig, ax = plt.subplots(figsize=(10,10))
ax.plot(x, y, label='observed')
ax.grid(True)
ax.set_title('coronavirus patients')

xticks = ['2020-02-01', '2020-03-01', '2020-04-01']
xlabels = ['2020-02', '2020-03', '2020-04']

ax.set_xticks(ticks=xticks)
ax.set_xticklabels(xlabels)

x = np.arange(0, len(y)+14)
y = (1.1 ** x) 
ax.plot(x, y, label='bad case until 2020-04-16')

ax.legend(loc='best')
fig.savefig('coronavirus_patients_2020-04-02.svg')

plt.show()

