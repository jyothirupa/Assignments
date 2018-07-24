# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 17:29:26 2018

@author: user
"""

string=input("Enter string:")
list1=[]
list1 = string.split()
wordfreq=[list1.count(p) for p in list1]
print(dict(zip(list1,wordfreq)))