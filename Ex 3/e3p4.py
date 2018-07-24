# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 14:48:07 2018

@author: user
"""

list1 = [int(x) for x in input("enter the elements of the list1:").split()]

print("Element 3: ", list1[2])
print("Element 6: ", list1[5])
print("First 5 elements: ")
for i in range(0,5):
    print(list1[i])
    
length = len(list1)
print("Last elements: ")
for i in range(6,length):
    print(list1[i])
    
list1[1] = 'x'
list1[4] = 'y'

print("After replacing: ", list1)

del(list1[4])
print("After deletion: ", list1)

print("Number of elements:", len(list1))