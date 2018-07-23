# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 23:12:38 2018

@author: Admin
"""

def count(string, length):
    vowel = "aeiouAEIOU"
    vowelCount = 0
    for i in range(0,length):
        for j in vowel:
            if string[i] == j:
                vowelCount = vowelCount + 1
    print("No of vowels:" + str(vowelCount))
    
string = input('enter a string:')
length = len(string)
count(string, length)

char = input('enter the character whose index is to be found:')
print(string.find(char))



