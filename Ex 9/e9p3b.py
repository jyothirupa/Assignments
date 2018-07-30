# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 06:24:58 2018

@author: Admin
"""

class Animal:
    def __init__(self):
        print("animal")
    
    def speak(self):
        print("speaking...")
        
class Dog(Animal):
    def __init__(self):
        print("dog")
    
    def speak(self):
        super().speak()
        print("barking...")
        
class Cat(Animal):
    def __init__(self):
        print("cat")
    
    '''
    def speak(self):
        super().speak()
        print("meowing...")
    '''
    
animalObj = Animal()
animalObj.speak()
    
obj1 = Dog()
obj1.speak()

obj2 = Cat()
obj2.speak()