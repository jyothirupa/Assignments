# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 19:57:13 2018

@author: Admin
"""
def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact = fact * i
    print("factorial = ", fact)

def lcm(x, y):
    if x > y:  
        greater = x  
    else:  
        greater = y  
    while(True):  
        if((greater % x == 0) and (greater % y == 0)):  
            lcmValue = greater  
            break  
        greater += 1

    print ("LCM of ", x, " and ", y, " = ", lcmValue)
    
def hcf(x, y):
    a = x
    b = y
    while(b != 0 ):
        t = b
        b = a % b
        a = t
    hcfValue = a
    print ("HCF of ", x, " and ", y, " = ", hcfValue)
      
def factor(x):
    print("The factors of ", x, " are:")
    for i in range(1, x + 1):
        if x % i == 0:
            print(i)
            
while 1:
    print("!:factorial 2:LCM 3:HCF 4:factors 5:exit")
    choice = int(input("enter the choice: "))
    if choice == 1:
        num = int(input("enter the number whose factorial is to be found: "))   
        factorial(num)
    
    elif choice == 2:
        print("enter the numbers whose LCM is to be found:")
        num1 = int(input("enter no 1:"))
        num2 = int(input("enter no 2:"))
        lcm(num1, num2)
    
    elif choice == 3:
        print("enter the numbers whose HCF is to be found:")
        num1 = int(input("enter no 1:"))
        num2 = int(input("enter no 2:"))
        hcf(num1, num2)
    
    elif choice == 4:
        num = int(input("enter the number whose factors are to be found: "))   
        factor(num)
        
    elif choice == 5:
        break
        

