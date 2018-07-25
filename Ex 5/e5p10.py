# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 12:06:40 2018

@author: user
"""

string = input("enter the word: ")
try:
    with open("C:/Users/user/Desktop/DigitalAlpha/file.txt", "r+") as f: 
       words = list((f.read()).split())
       #print(words)
       count = 0
       for word in words:
           if word == string:
               count += 1
       print("no of occurences: ", count)

except IOError:
    print("File does not exist")