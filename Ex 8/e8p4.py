# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 18:27:10 2018

@author: user
"""
def accept(row, col):
    a = []
    print(a)
    for i in range(row):
        b = []
        for j in range(col):
            ele = int(input("enter the element: "))
            b.append(ele)
        a.append(b)
    print(a)
    return a
        
def res(row, col):
    resultant = [[] for i in range(row)]
    for i in range(row):
        b = []
        for j in range(col):
            ele = 0
            b.append(ele)
        resultant[i] = b
    print(resultant)
    return resultant
    
print("matrix 1: ")
row1 = int(input("enter the no of rows: "))
col1 = int(input("enter the no of columns: "))

print("matrix 2: ")
row2 = int(input("enter the no of rows: "))
col2 = int(input("enter the no of columns: "))

if col1 != row2:
    print("matrix multiplication not possible")
    
else:
    mata = accept(row1, col1)
    matb = accept(row2, col2)
    result = res(row1, col2) 
    print(result)
    for i in range(row1):
        for j in range(col2):
            for k in range(row2):
                result[i][j] += mata[i][k] * matb[k][j]
    print(result) 
    