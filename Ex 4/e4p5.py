# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 17:04:27 2018

@author: user
"""

num = int(input("enter the number of key value pairs to be accepted:"))
dict1 = {}

'''
sumKey = 0
sumValue = 0
for i in range(num):
    key = int(input("enter the key: "))
    sumKey += key
    value = int(input("enter the value:"))
    sumValue += value
    dict1[key] = value
    
print("Sum of keys:", sumKey)
print("Sum of values:", sumValue)
'''

for i in range(num):
    key = int(input("enter the key: "))
    value = int(input("enter the value:"))
    dict1[key] = value
    
print(sum(dict1.values()))