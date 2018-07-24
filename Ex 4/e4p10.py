# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 17:38:03 2018

@author: user
"""

num = int(input("enter the number of key value pairs to be accepted:"))
dict1 = {}
for i in range(num):
    #key = input("enter the key: ")
    value = input("enter the value:")
    key = value[0]
    dict1[key] = value

print(dict1)