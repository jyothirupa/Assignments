# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 17:24:30 2018

@author: user
"""

list1 = [int(x) for x in input("enter the elements of the list1:").split()]
list2 = [int(x) for x in input("enter the elements of the list2:").split()]

dictionary = dict(zip(list1, list2))
print(dictionary)