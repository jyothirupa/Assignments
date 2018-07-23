# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 23:07:16 2018

@author: Admin
"""

def length(x):
    l=0
    while x!=0:
        l=l+1
        x=x//10
    return l
        
def calcSum(x,l):  
    sumArmstrong=0   
    while x!=0:
        sumArmstrong+=pow((x%10),l)
        x=x//10
    return sumArmstrong    
        
def armstrong(x):
    l=length(x)
    sumArmstrong=calcSum(x,l)
    if sumArmstrong == x:
        print(str(x) + ' is an armstrong number')
    else:
        print(str(x) + ' is not an armstrong number')
        
number=int(input("enter the number:"))
armstrong(number)
    
for i in range(1,501):
    armstrong(i)    