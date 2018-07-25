# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 11:36:18 2018

@author: user
"""

try:
    count = 0
    with open("C:/Users/user/Desktop/DigitalAlpha/file.txt", "r+") as f: 
        for line in f:
            words = line.split()
            count += len(words)
    
    print("no of words: ", count)
    
except IOError:
    print("File does not exist")