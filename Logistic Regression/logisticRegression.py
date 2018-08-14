# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 11:07:56 2018

@author: user
"""

import pandas as pd
from sklearn import linear_model
from sklearn.model_selection import train_test_split

df = pd.read_csv('C:/Users/user/.spyder-py3/Adult dataset/adult.csv')
#print(df.head())
#print(df.income.unique())

df["income"] = df["income"].map({ "<=50K": -1, ">50K": 1 })
y = df['income']
#print(y)

# create training and testing vars
X_train, X_test, y_train, y_test = train_test_split(df[['age', 'educational-num', 'hours-per-week']], y, test_size=0.2)
#print("Train shape: ", X_train.shape, y_train.shape)
#print("Test shape: ", X_test.shape, y_test.shape)

# fit a model
lm = linear_model.LogisticRegression()

model = lm.fit(X_train, y_train)
predictions = lm.predict(X_test)

print("Score: ", model.score(X_test, y_test))