# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 14:06:07 2018

@author: user
"""

listOfNumbers = [int(x) for x in input("enter the elements of the list:").split()]
newList = listOfNumbers.copy()
"""
maxNumber = listOfNumbers[0]
minNumber = listOfNumbers[0]
for listItem in listOfNumbers:
    if listItem < minNumber:
        minNumber = listItem
    elif listItem > maxNumber:
        maxNumber = listItem
print("Maximum value:" + str(maxNumber))
print("Minimum value:" + str(minNumber))
"""
length = len(listOfNumbers)
listOfNumbers.sort()
print("Largest value:", listOfNumbers[length-1])
print("Second largest value:", listOfNumbers[length-2])


length = len(newList)
first = newList[0]
newList[0] = newList[length-1]
newList[length-1] = first

"""
for listItem in listOfNumbers:
    print(listItem) 
"""

print(newList)
