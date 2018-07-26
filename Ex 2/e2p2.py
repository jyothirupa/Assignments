# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 23:07:38 2018

@author: Admin
"""

def factorial(x):
    if x == 0 | x == 1:
        return 1
    else:
        return x*factorial(x-1)
    
def fibonacci(x):
    if x<=1:
        return x
    else:
        return fibonacci(x-1)+fibonacci(x-2)

number=int(input("enter the number:"))
fact = factorial(number)
print(fact)
for i in range(0,number+1):
    print(fibonacci(i))
