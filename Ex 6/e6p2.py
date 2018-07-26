# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 14:49:39 2018

@author: user
"""

string = '#Python is an interpreted high level programming language for general-purpose programming*.'
newString = ''.join(e for e in string if e.isalnum() or e.isspace())
print("the string without special characters is: ", newString)

words = newString.split()
#print(word)

count = 0
for word in words:
    if word == word[::-1]:
        print(word, "is palindrome.")
        count += 1
if count == 0:
    print("there are no palindromes.")
    
wordFreq = [words.count(word) for word in words]        
wordDict = dict(zip(words, wordFreq))
#print(wordDict)

'''
wordDict = set(zip(words, wordFreq))
print(wordDict)
l = list(filter(lambda x:x[1]>1, wordDict))
print(l)
'''

for key, value in wordDict.items():
    if value > 1:
        print(key, " occurs ", value, " times.")
