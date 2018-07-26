# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 22:17:09 2018

@author: Admin
"""

string = input("enter the string:")
words = string.split(' ')
length = len(words)
print(length)
for i in range(0,length-1):
    for j in range(i+1,length):
        if words[i] > words[j]:
            temp = words[i]
            words[i] = words[j]
            words[j] = temp

for i in words:
    print(i)
            

"""
words.sort()
for i in words:
    print(i)
"""

