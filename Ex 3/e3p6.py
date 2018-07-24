# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 15:13:58 2018

@author: user
"""

list1 = [int(x) for x in input("enter the elements of the list1:").split()]
list2 = []
for i in range(0,len(list1)):
    list2.append(pow(list1[i],2))

finalList = zip(list1, list2)
print(sorted(list(finalList)))