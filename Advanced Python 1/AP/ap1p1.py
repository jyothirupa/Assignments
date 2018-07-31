# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 10:30:50 2018

@author: user
"""

import pandas as pd
from sklearn.datasets import load_boston

#import seaborn as sns
#df = sns.load_dataset('iris')

data = load_boston()
df = pd.DataFrame(data.data, columns=data.feature_names)

df["Target"] = data.target
print(df.head())

columnNames = list(df.head(0)) 
print()

print("the first two columns are: ", columnNames[0:2])
print()

print("data types of all columns: ")
print(df.dtypes)
print()

print("maximum value in column 1: ")
print(df[columnNames[1]].max())

print("minimum value in column 1: ")
print(df[columnNames[1]].min())
