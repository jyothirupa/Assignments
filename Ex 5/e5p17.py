# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 12:44:43 2018

@author: user
"""


filename = input("Enter file name: ")
for word in reversed(list(open(filename).read().split())):
    print(word.rstrip(), end=" ")
    