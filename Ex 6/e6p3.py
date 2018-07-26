# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 15:12:06 2018

@author: user
"""

a = {5, 3, 8, 6, 1}
b = {1, 5, 3, 4, 2}

union = a.union(b)
print("Union: ", union)

intersection = a.intersection(b)
print("Intersection: ", intersection)

print("Set differences:")
print("A-B: ", a-intersection)
print("B-A: ", b-intersection)

print("Maximum element in the set 'a': ", max(a))
print("Minimum element in the set 'a': ", min(a))

print("Maximum element in the set 'b': ", max(b))
print("Minimum element in the set 'b': ", min(b))