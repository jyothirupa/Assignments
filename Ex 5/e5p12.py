# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 12:15:59 2018

@author: user
"""

string = input("enter the letter: ")
try:
    with open("C:/Users/user/Desktop/DigitalAlpha/file.txt", "r+") as f: 
       letters = list(f.read())
       #print(letters)
       count = 0
       for letter in letters:
           if letter == string:
               count += 1
       print("no of occurences: ", count)

except IOError:
    print("File does not exist")