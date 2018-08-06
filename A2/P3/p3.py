# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 13:54:28 2018

@author: user
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('C:/Users/user/.spyder-py3/student.csv')
print(df)
print()

df = df.sort_values(by=['Height'])
print(df)
print()

df['bmi'] = df['Weight']/pow(df['Height']/100, 2)
print(df)
print()
df1 = df

df = df.groupby(['bmi'])
print(df)

healthy = []
over = []
obese = []
for i in range(0, len(df)):
    if df1['bmi'] <= 20:
        healthy.append(df1.iloc[i, 1])
    elif df1['bmi'] <= 30:
        over.append(df1.iloc[i, 1])
    else:
        obese.append(df1.iloc[i, 1])
    
print(healthy)
print(over)
print(obese)