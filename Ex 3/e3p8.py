# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 15:47:51 2018

@author: user
"""
import numpy as np 

coeff = [int(x) for x in input("enter the elements of the list1:").split()]
coeff.sort()
print(np.roots(coeff))
