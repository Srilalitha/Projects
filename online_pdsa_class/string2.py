# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 06:52:18 2020

@author: shanmukha
"""

# Write a function elminate_letter(word, letter), which takes a word
# and a letter as arguments and removes all the occurrences of that particular 
# letter from the word, the function will return the remainig letters in the word"

def eliminate_letter(word, letter):
    print("String = ", word)
    print("After Removing letter : ",letter )
    print("String = ", end=' ')
    newstr= word.replace(letter, " ")
    return newstr
x=eliminate_letter('python programming', 'p')
print(x)

# Write a funtion to convert all vowels to uppercase in a given string
def UpperCaseVowels(word):
    newstr=' '
    print("String = ", word)
    print("After Changing case of Vowels " )
    print("String = ", end=' ')
    for i in word:
        if(i == 'a' or i == 'e' or i=='i' or i=='o' or i=='u'):
            newstr = newstr +' '  + i.upper()
        else:
            newstr = newstr + i 
    return newstr
s="I am liking Python Coding, online tutorials are very helpful"
print(UpperCaseVowels(s))

#Write a function which removes all the vowels and returns the remaining letters
def RemoveVowels(word):
    newstr=' '
    print("String = ", word)
    word=word.lower()
    print("After Removing  Vowels " )
    print("String = ", end=' ')
    for i in word:
        if(i != 'a' and i != 'e' and i!='i' and i!='o' and i!='u'):
            newstr = newstr + i 
    return newstr

s="I am liking Python Coding, online tutorials are very helpful"
print(RemoveVowels(s))

