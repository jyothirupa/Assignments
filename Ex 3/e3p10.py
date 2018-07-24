# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 16:17:05 2018

@author: user
"""

list1 = [int(x) for x in input("enter the elements of the list1:").split()]
list2 = []

for i in range(0,len(list1)):
    total = 0
    for j in range(0,i+1):
        total += list1[j]
    list2.append(total)
    
print(list2)