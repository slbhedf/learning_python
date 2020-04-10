# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

density_filename = 'densities_by_prefectures.csv'
confirmed_filename = 'confirmed_cases_by_prefectures.csv'

density_df = pd.read_csv(density_filename,encoding='utf8')
confirmed_df = pd.read_csv(confirmed_filename, encoding='utf8')

prefectures = {}

for i in density_df.index:
    name = density_df['Prefecture'][i]
    prefectures[name] = {'Density': density_df['Density'][i] } 

for i in confirmed_df.index:
    name = confirmed_df['Prefecture'][i]
    prefectures[name]['Confirmed'] = confirmed_df['Confirmed'][i] 
    
df = pd.DataFrame(prefectures).transpose()
print(df.corr())

fig = plt.figure()
ax = fig.subplots()
x = df[['Density']]
y = df[['Confirmed']]
ax.scatter(x, y)

reg = LinearRegression()
reg.fit(x, y)
ax.plot(x, reg.predict(x))

fig.savefig('density_confirmedcase.svg')
plt.show()

