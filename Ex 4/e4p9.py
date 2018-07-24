# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 17:40:16 2018

@author: user
"""
'''
dict1 = {'Zara' : 23, 'Bran' : 78, 'Charlie' : 34, 'Kate' : 90, 'Monica' : 88}
'''
num = int(input("enter the number of key value pairs to be accepted:"))
dict1 = {}

for i in range(num):
    key = input("enter the key: ")
    value = int(input("enter the value:"))
    dict1[key] = value
    
dict2 = {}

listOfValues = list(dict1.values())
print(listOfValues)
listOfValues.sort()
print(listOfValues)

for i in range(0,len(listOfValues)):
    for key, value in dict1.items():    
        if listOfValues[i] == value:
            temp = {key : value}
            dict2.update(temp)

print(dict2)
