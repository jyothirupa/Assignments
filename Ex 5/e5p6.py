# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 11:22:42 2018

@author: user
"""
try:
    fp = open("C:/Users/user/Desktop/DigitalAlpha/file.txt", "r+")
    string = fp.read()
    print("File contents:")
    print(string)
except IOError:
    print("File does not exist")