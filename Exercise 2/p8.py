# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 13:41:11 2018

@author: user
"""

lines = []
while True:
    line = input("enter the input text:")
    if line:
        lines.append(line)
    else:
        break
text = '\n^^^'.join(lines)
print('^^^',end="")
print(text)

