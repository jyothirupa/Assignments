# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 23:08:20 2018

@author: Admin
"""

string = input('enter the string:')
length = len(string)
char=0
upper=0
lower=0
digit=0
for i in range(0,length):
    if string[i].isalpha():
        char=char+1
        if string[i].isupper():
            upper=upper+1
        elif string[i].islower():
            lower=lower+1
    elif string[i].isdigit():
        digit=digit+1
print('No of Upper case letters:'+str(upper))
print('No of Lower case letters:'+str(lower))
print('No of Characters:'+str(char))
print('Length of string:'+str(length))
print(string+'ing')
newString=""
newString=newString+string[0]
for i in range(1,length):
    if string[i] != string[0]:
        newString=newString+string[i]
    else:
        newString=newString+'$'
print(newString)