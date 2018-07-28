# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 17:41:48 2018

@author: user
"""

num = int(input("enter the no of students: "))

result = ()

for i in range(0,num):
    w = int(input("enter the weight: "))
    h = int(input("enter the height: "))
    tup = (w, h, (w / pow(h, 2)))
    result = result + (tup,) 
    
print(result)
    