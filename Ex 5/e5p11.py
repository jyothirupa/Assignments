# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 12:00:42 2018

@author: user
"""

try:
    fp1 = open("C:/Users/user/Desktop/DigitalAlpha/file.txt", "r+")
    fp2 = open("C:/Users/user/Desktop/DigitalAlpha/copiedFile.txt", "w+")
    fp2.write(fp1.read())
    fp1.close()
    fp2.close()
    fp2 = open("C:/Users/user/Desktop/DigitalAlpha/copiedFile.txt", "r+")
    print("Content:")
    print(fp2.read())
    fp2.close()
    
except IOError:
    print("file does not exist")