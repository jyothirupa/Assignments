# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 09:28:04 2018

@author: user
"""

string = input("enter the comma separated sequence of words: ")
words = string.split(",")

sortedWords = sorted(words)
print(sortedWords)

#sort is in-place therefore the following doesn't work
#print(words.sort())

#alternative solution
words.sort()
print(words)
