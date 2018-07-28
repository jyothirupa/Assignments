# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 09:38:02 2018

@author: user
"""

password = input("enter the password: ")
length = len(password)

def check(word):
    capital = False
    number = False
    specialChar = False
    for char in word:
        if char.isupper():
            capital = True
        elif char.isdigit():
            number = True
        else:
            specialChar = True
    if capital and number and specialChar:
        return True
    else:
        return False

if length > 8 and length < 15 and check(password):
    print("password valid.")
    
else:
    print("password invalid.")
