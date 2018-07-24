# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 15:25:55 2018

@author: user
"""
import random

list1 = [int(x) for x in input("enter the elements of the list1:").split()]

num = int(input("how many random numbers do you want to append?"))
for x in range(num):
    list1.append(random.randint(1,20))
        
print(list1)
  

