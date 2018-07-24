# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 14:58:49 2018

@author: user
"""

list1 = [int(x) for x in input("enter the elements of the list1:").split()]
num = int(input("enter an element:"))

"""
def countOccurrence(lists, num):
    count = 0
    for i in lists:
        if num in lists:
            count += 1
    print(num, "occurs ", count, " times in the list")
    
countOccurrence(list1,num)
"""

print("Number of occurrences:", list1.count(num))

length = len(list1)
odd = []
even = []

for i in list1:
    if(i%2==0):
        even.append(i)
    else:
        odd.append(i)
even.sort()
odd.sort()
count1=0
count2=0
for k in even:
    count1=count1+1
for j in odd:
    count2=count2+1
print("Largest even number:",even[count1-1])
print("Largest odd number",odd[count2-1])