# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 14:31:51 2018

@author: user
"""

a = [['Rhia',10,20,30,40,50], ['Alan',75,80,75,85,100], ['Smith',80,80,80,90,95]]

#print(type(a))
list1 = []
for i in a:
    list1.append(i[0:2])

print("the original list is: ", a)
print("the sliced list is: ", list1)

a[2] = ['Sam',82,79,88,97,99]
print("the updated list is: ", a)

a[0][3] = 95
print("the updated list is: ", a)

content = [73, 80, 85]
for i, j in zip(a, content):
        i.append(j)
print("the updated list is: ", a)



