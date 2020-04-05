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
    x.append(d.strftime("%d %b"))
    y.append(n)
    d = d + timedelta(days=1)

fig, ax = plt.subplots(figsize=(20,20))
ax.plot(x, y, label='observed')
ax.grid(True)
ax.set_title('coronavirus patients')


# predict
#c  = curve_fit(lambda t,c1,c2,c3: c1*(c2**t)+c3,  np.arange(len(y)-10,len(y)),  y[-10:])
c  = curve_fit(lambda t,c1,c2,c3: c1*(c2**t)+c3,  np.arange(0, len(y)),  y)
x2 = np.arange(0, len(y)+30)
y2 = c[0][0] * (c[0][1] ** x2) + c[0][2]
ax.plot(x2, y2, label='bad case', lw=0.5)
print("y={}*({}**x)+{}".format(c[0][0], c[0][1], c[0][2]))

# xtick labels
d = date_list[0]
date_until = datetime(2020, 5, 4)
xticks = []
xlabels = []
i = 0
while(d< date_until):
    xticks.append(i)
    xlabels.append(d.strftime("%d %b"))
    d = d + timedelta(days=1)
    i += 1

ax.set_xticks(ticks=xticks)
ax.set_xticklabels(xlabels)

ax.legend(loc='best')
plt.xticks(rotation=70)
plt.tight_layout()

fig.savefig('svg/coronavirus_patients_tokyo.svg')
plt.show()
