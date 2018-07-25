# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 12:32:25 2018

@author: user
"""

try:
    with open("C:/Users/user/Desktop/DigitalAlpha/file.txt", "r+") as f: 
       letters = list(f.read())
       #print(letters)
       count = 0
       for letter in letters:
           if letter == " ":
               count += 1
       print("no of occurences: ", count)

except IOError:
    print("File does not exist")