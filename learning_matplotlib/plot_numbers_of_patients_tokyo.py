'''
plot the numbers of coronavirus patients in tokyo.
download the csvfile

URL: https://stopcovid19.metro.tokyo.lg.jp/data/130001_tokyo_covid19_patients.csv

I also predit the numbers of patients in a bad case.
'''

import pandas as pd
from datetime import timedelta, datetime
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

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

fig, ax = plt.subplots(figsize=(10,10))
ax.plot(x, y, label='observed')
ax.grid(True)
ax.set_title('coronavirus patients')


# predict
c  = curve_fit(lambda t,a,b: a*(b**t),  np.arange(0,len(y)),  y)
x2 = np.arange(0, len(y)+30)
y2 = c[0][0] * (c[0][1] ** x2) 
ax.plot(x2, y2, label='bad case', lw=0.5)

# xtick labels
m2 = datetime(2020,2,1) - date_list[0]
m3 = datetime(2020,3,1) - date_list[0]
m4 = datetime(2020,4,1) - date_list[0]
m5 = datetime(2020,5,1) - date_list[0]

xticks = [m2.days, m3.days, m4.days, m5.days]
xlabels = ['2020-02', '2020-03', '2020-04', '2020-05']
ax.set_xticks(ticks=xticks)
ax.set_xticklabels(xlabels)

ax.legend(loc='best')
fig.savefig('coronavirus_patients_2020-04-02.svg')
plt.show()
