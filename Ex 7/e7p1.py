# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 17:56:15 2018

@author: user
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
        sumArmstrong+=pow((x % 10), l)
        x=x//10
    return sumArmstrong    
        
def armstrong(x):
    l=length(x)
    sumArmstrong=calcSum(x,l)
    if sumArmstrong == x:
        print(x, ' is an armstrong number.')
                
for i in range(1,1001):
    armstrong(i)    