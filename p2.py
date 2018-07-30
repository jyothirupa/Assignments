# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 16:25:18 2018

@author: user
"""
import statistics
from operator import itemgetter  

print("Enter the name and marks of 5 student: ")
numberOfStudents = 5
studentList = []
students = []
marks1 = []
marks2 = []
marks3 = []
total = []
for i in range(0, numberOfStudents):
    marks = []
    nm = input("enter the name: ")
    mk1 = int(input("enter the marks 1: "))    
    marks1.append(mk1)
    mk2 = int(input("enter the marks 2: "))    
    marks2.append(mk2)
    mk3 = int(input("enter the marks 3: "))
    marks3.append(mk3)
    totalMarks = mk1 + mk2 + mk3
    total.append(totalMarks)
    marks.append(totalMarks)
    marks.append(mk1)
    marks.append(mk2)
    marks.append(mk3)
    
    studentList.append((nm,marks))

students = dict(studentList)
print(students)
print()

print("Mean 1: ", statistics.mean(marks1))
print("Mean 2: ", statistics.mean(marks2))
print("Mean 3: ", statistics.mean(marks3))
print()

print("Median 1: ", statistics.median(marks1))
print("Median 2: ", statistics.median(marks2))
print("Median 3: ", statistics.median(marks3))
print()

sortedList = sorted(students.items(), key = itemgetter(1), reverse = True)
print("name\t[total, subject 1, subject 2, subject 3]")
for key, value in sortedList:
    print(key, " ", value)   
print()

sortedTotal = sorted(total)
top = [sortedTotal[len(sortedTotal) - 1], sortedTotal[len(sortedTotal) - 2], sortedTotal[len(sortedTotal) - 3]]

print("Top 3:")
for i in range(0, 3):
    for key, value in students.items():
        if value[0] == top[i]:
            print(key, " ", value)
print()
           
for key, value in sortedList:
    if value[0]//3 > 90:
        print(key, " ", value[0], " A+")
    elif value[0]//3 > 80:
        print(key, " ", value[0], " A")
    elif value[0]//3 > 70:
        print(key, " ", value[0], " B+")
    elif value[0]//3 > 60:
        print(key, " ", value[0], " B")
    elif value[0]//3 > 50:
        print(key, " ", value[0], " C")
    else:
        print(key, " ", value[0], " D")
    

    
        

    

    
    
    
    