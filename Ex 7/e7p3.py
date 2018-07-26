# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 18:27:15 2018

@author: user
"""

num = int(input("enter the number of key value pairs to be accepted:"))

dict1 = {}
for i in range(num):
    key = int(input("enter the number: "))
    value = pow(key, 2)
    dict1[key] = value
    
print(dict1)