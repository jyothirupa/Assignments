# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 11:47:08 2018

@author: user
"""

try:
    count = 0
    with open("C:/Users/user/Desktop/DigitalAlpha/file.txt", "r+") as f: 
        for line in f:
            count += 1
    
    print("no of lines: ", count)
    
except IOError:
    print("File does not exist")