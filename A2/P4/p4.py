# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 16:03:43 2018

@author: user
"""
import numpy as np
from numpy import newaxis

x = np.array([[1, 2, 3], [4, 5, 6]], np.int32)
print("Array")
print(x)
print()

print("Shape")
print(x.shape)
print()

print("converting to 3D")
y = x[:, :, newaxis]
print(y)
print("Shape: ", y.shape)
print()

print("after addition")
add = np.array([[5, 5, 5], [5, 5, 5]], np.int32)
summation = x + add
print(summation)
print()

print("after subtraction")
sub = np.array([[2, 2, 2], [2, 2, 2]], np.int32)
result = x - sub
print(result)
print()

print("after multiplication")
mul = np.array([[5, 5, 5], [5, 5, 5]], np.int32)
prod = x * mul
print(prod)
