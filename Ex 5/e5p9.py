# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 11:49:31 2018

@author: user
"""

string = input("enter the string to be appended: ")
try:
    with open("C:/Users/user/Desktop/DigitalAlpha/file.txt", "a+") as f: 
        f.write(string)
        
    with open("C:/Users/user/Desktop/DigitalAlpha/file.txt", "r+") as f:
        print("Content:")
        print(f.read())

except IOError:
    print("File does not exist")
    