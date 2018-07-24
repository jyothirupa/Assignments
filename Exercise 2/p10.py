# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 23:37:14 2018

@author: Admin
"""

def uniqueSort(x):
    words = x.split(',')
    print(",".join(sorted(list(set(words)))))
    
string = input("enter the string:")
uniqueSort(string)
