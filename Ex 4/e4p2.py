# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 16:32:07 2018

@author: user
"""

dict1 ={11 : 'Anil', 12 : 'Amit', 13 : 'Brook', 14 : 'Charlie', 15 : 'Sunil'}
dict2 ={21 : 'Anil', 22 : 'Amit', 23 : 'Brook', 24 : 'Charlie', 25 : 'Sunil'}

dictSum = {}
dictSum.update(dict1)
dictSum.update(dict2)
print(dictSum)