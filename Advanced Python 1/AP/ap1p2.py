# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 09:20:07 2018

@author: user
"""

import numpy as np

#2D array
def accept(row, col):
    a = []
    for i in range(row):
        b = []
        for j in range(col):
            ele = int(input("enter the element: "))
            b.append(ele)
        a.append(b)
    return a

r = int(input("enter the number of rows: "))
c = int(input("enter the number of columns: "))
my_array = np.array(accept(r, c))

print("array: ")
print(my_array)

print("shape of array: ")
print(my_array.shape)

print("reshaped array: ")
print(my_array.reshape(c, r))

print("shape of array: ")
print(my_array.shape)

print("slicing the array: ")
print(my_array[0:2,1]) #Select items at row 0 and 1, column 1

print("convert to 1D array: ")
print(my_array.flatten()) #ravel() - 1D view, flat() - 1D iterator & flatten() - 1D copy

print("sum of array elements: ")
print(np.sum(my_array))

print("minimum element of array: ")
print(my_array.min())

print("maximum element of array: ")
print(my_array.max())

row = int(input("enter the number of rows: "))
col = int(input("enter the number of columns: "))
new_array = np.array(accept(row, col))

print("sum of the arrays: ")
print(np.add(my_array, new_array)) 

print("product of the arrays: ")
print(np.multiply(my_array, new_array))

print("quotient of the arrays: ")
print(np.divide(my_array, new_array))
