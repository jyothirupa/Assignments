# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

string = input("enter the string:")
length = len(string)
newString = ""
newString = newString + string[length-1]
for i in range(1,length-1):
    newString = newString + string[i]
newString = newString + string[0]
print("Original string:" + string)
print("Modified string:" + newString)

