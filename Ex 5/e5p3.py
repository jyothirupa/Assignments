# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 11:13:13 2018

@author: user
"""

string1 = input("enter the 1st string: ")
letters1 = set(string1.lower())

string2 = input("enter the 2nd string: ")
letters2 = set(string2.lower())

intersection = letters1.intersection(letters2)

print("A-B: ", letters1.difference(intersection))