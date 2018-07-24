# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 15:54:50 2018

@author: user
"""

low = int(input("enter the lowest number of range:"))
high = int(input("enter the highest number of range:"))

"""
def perfectSq(num): 
    if num/math.sqrt(num) == math.sqrt(num):
        print("Sq root:", math.sqrt(num))
        print("Number:", num)

for i in range(low,high+1):
    perfectSq(i)
"""
def sumCheck(n):
    number = n
    total = 0
    while n != 0:
        digit = n%10
        total += digit
        n=n//10
    if total < 10:
        print(number, " has sum less than 10")

print("The perfect squares are:")
def perfectSq(num): 
    for i in range(1,num+1):
        if pow(i,2) == num:
            print(num)
            sumCheck(num)
            
for i in range(low,high+1):
    perfectSq(i)