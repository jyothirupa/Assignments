# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 16:59:05 2018

@author: user
"""

low = int(input("enter the lowest number of range:"))
high = int(input("enter the highest number of range:"))

num = int(input("enter the number of key value pairs to be accepted:"))

dict1 = {}
for i in range(num):
    key = int(input("enter the number: "))
    if i in range(low, high+1):
        value = pow(key, 2)
        dict1[key] = value
    
print(dict1)