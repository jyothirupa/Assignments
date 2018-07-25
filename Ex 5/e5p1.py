# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 10:52:06 2018

@author: user
"""
'''
list1 = [int(x) for x in input("enter the elements of the set:").split()]
set1 = set(list1)
'''
string = input("enter the string: ")
letters = set(string.lower())
print(letters)

vowel = "aeiou"
count = 0
for letter in letters:
    for x in vowel:
        if letter == x:
            count += 1
            
print("no of vowels = ", count)