# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 15:24:09 2018

@author: user
"""
primes = []
for number in range(900, 1001):
    flag = 0
    for i in range(2, number):
        if (number % i) == 0:
            flag = 1
            break
    if flag == 0:
        primes.append(number)   

print("the prime numbers are: ", primes)

count = 0
for num in primes:
    temp = num
    rev = 0
    while temp != 0:
        rev = (rev * 10) + (temp % 10)
        temp = temp // 10
        
    if num == rev:
        print(num, "is a palindrome.")
        count += 1
        
if count == 0:
    print("there are no palindrome prime numbers between 900 and 1000.")