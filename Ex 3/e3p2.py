# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 14:21:06 2018

@author: user
"""

list1 = [int(x) for x in input("enter the elements of the list1:").split()]
list2 = [int(x) for x in input("enter the elements of the list2:").split()]

mergedList = list1 + list2
print("Merged list:", mergedList)

mergedList.sort()
print("Sorted merged list:", mergedList)
