# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 09:34:58 2018

@author: user
"""

while(True):
    numberOfSentences = int(input("enter the number of sentences: "))
    if numberOfSentences < 4:
        print("enter atleast 4 sentences.")
    else:
        break

paragraph = []  
for i in range(0, numberOfSentences):
    sent = input("enter the sentence: ")
    paragraph.append(sent)

for i in range(0, numberOfSentences):
    print(paragraph[i], end="")
print()
print()
    
index = numberOfSentences // 2

paragraph[index] = "UST Global specializes in healtcare, retail & customer goods, banking & financial services, telecom, media and technology, insurance, transportation & logistics and manufacturing & utilities."

for i in range(0, numberOfSentences):
    print(paragraph[i], end="") 
print()
print()

paragraphCopy = paragraph

for i in range(0, numberOfSentences):
     paragraphCopy[i].lower()
    
vowel = "aeiou"
noOfVowels = 0
lower = 0
upper = 0
specialCharacter = 0
for i in range(0, numberOfSentences):
    for char in list(paragraphCopy[i]):
        for letter in vowel:
            if char == letter:
                noOfVowels += 1
        if char.islower():
            lower += 1
        elif char.isupper():
            upper += 1
        elif char.isdigit():
            continue
        else:
            specialCharacter += 1
            
print("no of vowels = ", noOfVowels)
print("no of lower case characters = ", lower)
print("no of upper case characters = ", upper)
print("no of special characters = ", specialCharacter)
print("no of vowels = ", noOfVowels)

string = ""
for i in range(0, numberOfSentences):
    string = string + paragraphCopy[i]

newString =""
for char in list(string):
    if char == '.':
        newString = newString + '. ' 
    else:
        newString = newString + char

stringFinal = ""
for i in range(0, len(newString)):
    if newString[i].isalpha() or newString[i].isdigit():                 
        stringFinal = stringFinal + newString[i]
    else:
        continue        
print()        
print("String without special characters= ", stringFinal)
print()

dictWords = []
words = newString.split()
for word in words:
    freq = words.count(word)
    dictWords.append((word, freq))
    
dictionary = dict(dictWords)        
print(dictionary)
print()

for key, value in dictionary.items():
    if value > 1:
        print (key, " is present ", value, " times.")
        
finalList = []
finalList.append(paragraphCopy[numberOfSentences - 1])
for i in range(1, numberOfSentences - 1):
    finalList.append(paragraphCopy[i])
finalList.append(paragraphCopy[0])

string1 = ""
for i in range(0, len(finalList)):
    string1 = string1 + finalList[i]

newString1 =""
for char in list(string1):
    if char == '.':
        newString1 = newString1 + '. ' 
    else:
        newString1 = newString1 + char
        
print()
print("After swapping: ", newString1)

    



