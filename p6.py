# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 21:59:40 2018

@author: Admin
"""

def reverse(string):
    string = "".join(reversed(string))
    return string

def checkLength(s):
    if s % 4 == 0:
        print("Multiple of 4")
    else:
        print("Not a multiple of 4")
  
string = input("enter a string:")
reversedString = reverse(string)
print(reverse(string))
checkLength(len(string))
