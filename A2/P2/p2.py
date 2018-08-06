# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 15:04:06 2018

@author: user
"""
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('C:/Users/user/.spyder-py3/camera.csv')

print("Properties of the dataset: ")
for i in df.columns:
    print(i)
print()

print("Data types of properties of the dataset: ")
print(df.dtypes)
print()

print(df.iloc[0:26, [0, 1, 12]])

print("Summary: ")
print(df.describe())

s = pd.Series(df['Price'])
print(s.describe())