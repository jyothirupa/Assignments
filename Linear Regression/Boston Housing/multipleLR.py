# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 10:14:27 2018

@author: user
"""

from sklearn import linear_model
from sklearn import datasets
import pandas as pd

data = datasets.load_boston()

df = pd.DataFrame(data.data, columns=data.feature_names)

target = pd.DataFrame(data.target, columns=['MEDV'])

X = df[['RM', 'PTRATIO', 'LSTAT']]
y = target['MEDV']

lm = linear_model.LinearRegression()

model = lm.fit(X,y)

predictions = lm.predict(X)

#print(predictions[0:5])
print("R^2 = ", lm.score(X,y))
