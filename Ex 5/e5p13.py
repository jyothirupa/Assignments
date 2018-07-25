# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 12:18:06 2018

@author: user
"""
import re

try:
    with open("C:/Users/user/Desktop/DigitalAlpha/file.txt", "r+") as f: 
       content = f.read()
       r = r'[0-9]+'
       num = re.findall(r, content)
       print(set(num))       
       
except IOError:
    print("File does not exist")