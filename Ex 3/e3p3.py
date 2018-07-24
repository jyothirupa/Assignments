# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 14:43:07 2018

@author: user
"""

list1 = [int(x) for x in input("enter the elements of the list1:").split()]
list2 = [int(x) for x in input("enter the elements of the list2:").split()]

print(list(set().union(list1, list2)))

print(list(set(list1).intersection(list2)))