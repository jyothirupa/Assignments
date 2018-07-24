# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 16:36:18 2018

@author: user
"""
num = int(input("enter the number of key value pairs to be accepted:"))
dict1 = {}
for i in range(num):
    key = input("enter the key: ")
    value = input("enter the value:")
    dict1[key] = value
    
#dict = {'Name': 'Zara', 'Age': 27, 'Job description': 'SE', 'DOB': '7 July 1990'}
key = input("Enter the key to be searched:")
print ("Value : %s" %  dict1.get(key, "Not available"))