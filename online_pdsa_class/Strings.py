# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 22:52:54 2020

@author: shanmukha
"""

#String Operations

# Python string examples - all assignments are identical.
String_var1 = 'Python'
String_var2 = "Python"
String_var3 = """Python"""

print(String_var1)
# with Triple quotes Strings can extend to multiple lines
String_var = """ This document will help you to explore all the concepts of Python Strings!!! """

# Replace "document" with "tutorial" and store in another variable
substr_var = String_var.replace("document", "tutorial")
print (substr_var)

dialogue = '''He said his favourite book is
"Hitchhiker's Guide to the Galaxy”'''
print(dialogue)

#indexing a string
sample_str = 'Python String'
print (sample_str[0])      
 # return 1st character           # output: P
print (sample_str[-1])      
# return last character           # output: g
print (sample_str[-2])      
# return last second character    # output: n

print(sample_str[0:len(sample_str):2])
print(sample_str)
print("String" in sample_str)

print(len(sample_str))


#slicing a string
sample_str = 'Python String'
print (sample_str[3:5])	    #return a range of character
# ho
print (sample_str[7:])      # return all characters from index 7
# String
print (sample_str[:6])      # return all characters before index 6
# Python
print (sample_str[7:-4])
# St
type(sample_str) is str

#Modify / Delete a string
sample_str = 'Python String'
sample_str[2] = 'a'

# TypeError: 'str' object does not support item assignment

sample_str = 'Programming String'
print (sample_str)

# Output=> Programming String

#Python Strings are by design immutable. 
#It suggests that once a String binds to a variable, it can’t be modified.

#We cannot modify Strings by deleting some characters from it. 
#Instead, we can remove the Strings altogether by using the ‘del’ command.

sample_str = "Python is the best scripting language."
del sample_str[1]
# TypeError: 'str' object doesn't support item deletion

del sample_str
print (sample_str)
# NameError: name 'sample_str' is not defined

print ("Employee Name: %s,\nEmployee Age:%d" % ('Ashish',25))

#String function
str1 = "C  C++  Java  Python"
str2 = str1.split()
print(str2)

str2 = "abc."
print(str2.isalpha())

s1="Welcome to Java Programming"
s2=s1.replace("Java","Python")
print(s1)
print(s2)
print(s2[:-1])

s='ABBCCDEEBBFFERBBJJUIBB'
print(s.count("BB"),end=' ')
print(s.count("BB",1),end=' ')
print(s.count("BB",2),end=' ')
print(s.count("BB",3),end=' ')

s="ILOVEWORLD"
for ch in range(0,len(s),3):
    print(s[ch], end=' ')
    
print(s)
print(s[:-1])
print(s[:len(s)])
print(s[len(s):])

def countbc(word):
    print(word)
    cnt = 0
    for bc in word:
        print(bc)
        if(bc == 'bc'):
            cnt = cnt + 1
    return cnt
print("Number of 'bc' = ", countbc("abcbabcaaa"))

word="abcbabcaaa"
print(word.count('bc'))