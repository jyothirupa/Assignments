# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 12:44:43 2018

@author: user
"""


filename = input("Enter file name: ")
#for word in reversed(list(open(filename).read())):
#    print(word.rstrip(), end=" ")
fp = open(filename, "rb+")
fp.seek(0, 2)
pos = -fp.tell()
for i in range(-1,(pos-1),-1):
    fp.seek(i,2)
    print((fp.read(1)).decode(), end="")
fp.close()
    

    