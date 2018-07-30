# -*- coding: utf-8 -*-
"""
Created on Sun Jul 29 19:00:38 2018

@author: Admin
"""
import math

class Area:
    def __init__(self):
        print("base class")
    
    def calcArea():
        print("area here...")
        
class Triangle(Area):
    def __init__(self, base, height):
        self.__base = base
        self.__height = height
        print("triangle")
    
    def calcArea(self):
        print("area = ", 0.5 * self.__base * self.__height)
        
class Rectangle(Area):
    def __init__(self, length, breadth):
        self.__length = length
        self.__breadth = breadth
        print("rectangle")
    
    def calcArea(self):
        print("area = ", self.__length * self.__breadth)
        
class Circle(Area):
    def __init__(self, radius):
        self.__radius = radius
        print("circle")
    
    def calcArea(self):
        print("area = ", math.pi * pow(self.__radius, 2))

obj1 = Triangle(4, 3)
obj1.calcArea()

obj2 = Rectangle(3, 1.5)
obj2.calcArea()

obj3 = Circle(2)
obj3.calcArea()