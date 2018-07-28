# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 17:36:55 2018

@author: user
"""
import math

num = int(input("enter the number: "))
dict1 = {}

for i in range(1, num + 1):
    area = math.pi * pow (i, 2)
    dict1[i] = area

print(dict1)