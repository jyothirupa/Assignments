# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 17:18:39 2018

@author: user
"""

num = int(input("enter the number of key value pairs to be accepted:"))
dict1 = {}
prod = 1
for i in range(num):
    key = int(input("enter the key: "))
    value = int(input("enter the value:"))
    prod *= value
    dict1[key] = value
    
print(prod)
    
