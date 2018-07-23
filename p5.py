# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 21:24:33 2018

@author: Admin
"""

def removeOdd(x, length):
    for i in range(0,length):
        if i % 2 == 0:
            continue
        else:
            print(x[i], end='')

def numberOccurences(x):
    count = dict()
    words = x.split(' ')
    for word in words:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    return count
            
string = input("enter the string:")
length = len(string)
print(removeOdd(string, length))
print()
print(numberOccurences(string))

    
    