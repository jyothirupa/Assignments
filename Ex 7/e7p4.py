# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 19:35:11 2018

@author: Admin
"""

string = input("enter the string: ")
noOfLetters = 0
noOfDigits = 0
for char in string:
    if char.isalpha():
        noOfLetters += 1
    elif char.isdigit():
        noOfDigits += 1

print("number of letters = ", noOfLetters)
print("number of digits = ", noOfDigits)
    
    
