# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 14:49:41 2018

@author: user
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('C:/Users/user/.spyder-py3/100 Sales Records.csv')
print(df.columns)
print()

print(df.loc[0:9, 'Region':'Unit Price'])

df1 = pd.DataFrame(df['Total Profit'], columns = ['Total Profit'])
plt.figure()
df1.plot.hist(alpha=0.5)
plt.xlabel('Total Profit')
plt.show()

print()
print(df.loc[df['Total Cost'] > 1000000]['Item Type'])

