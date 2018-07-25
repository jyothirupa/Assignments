# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 12:34:50 2018

@author: user
"""

try:
    with open("C:/Users/user/Desktop/DigitalAlpha/file.txt", "r+") as f: 
       content = f.read()
     
    with open("C:/Users/user/Desktop/DigitalAlpha/file.txt", "w+") as f:
        
       f.write(content.title())
   
    with open("C:/Users/user/Desktop/DigitalAlpha/file.txt", "r+") as f:         
       print(f.read())

except IOError:
    print("File does not exist")