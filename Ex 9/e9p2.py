# -*- coding: utf-8 -*-
"""
Created on Sun Jul 29 18:06:53 2018

@author: Admin
"""

class Employee:
    def __init__(self):
        self.str1 = "Employee"
        print("I am an employee.")
        
class FullTime(Employee):
    def __init__(self):
        Employee.__init__(self)
        self.str2 = "Full time"
        print("I am a full time employee.")
        
class PartTime(Employee):
    def __init__(self):
        Employee.__init__(self)
        self.str3 = "Part time"
        print("I am a part time employee.")
        
class Intern(FullTime, PartTime):
    def __init__(self):
        FullTime.__init__(self)
        PartTime.__init__(self)
        print("I am an intern.")
        
    def printStr(self):
        print(self.str2, self.str3)
    
        
obj = Intern()
obj.printStr()