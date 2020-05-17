# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 17:58:50 2020

@author: shanmukha
"""
L1 = list()

type(L1)

L5 = [5, [2, ["Java", "Python"]], 75000.00]
print(L5[1][1][1][2:4])             # to extrach th in python

l1 = [10,20,30,40,50,60]
l3=l1[1:4]
l2=l1[0]
print(type(l3))
print(type(l2))


s = "hello world"
s[1:4]
s[::-1]
s[:-1]
s[::]
s[:len(s)-1]

l1 = ['a','b','c','d']
l1 = [x for x in l1 if ord(x) > 98]
print(l1)

l1 = ['a','b','c','d']
l1 = [x for x in l1 if ord(x) > 98]
print(l1)

l2 = ['a','b','c','d','e','f','g','h','i','j']
print( l2[0:2])
l1 = ['a','b','c','d']
print(l1[::-1])

l2 = l2 + l1
print(l2)

l1 = [[n,n+1,n+2] for n in range(0,3)]
print(l1)

l1=[10,30]
l2 = l1
l1[1]=20
print(l1, l2)

l5 = ['a','b','c']
l6 = ['e','b','c']
print(l5==l6)

list_a = [11, 16, 21, 26, 31, 36, 41]
list_b = [26, 41, 36]
list_out = list_a - list_b
print(list_out)

def a(list1, list2):
    out = [item for item in list1 if not item in list2]
    return out

# Test Input
list1 = [11, 16, 21, 26, 31, 36, 41] 
list2 = [26, 41, 36] 

# Run Test
print(a(list1, list2)) 


vowels = ['a','e','i','o','u']
vowels.remove('a')
# Result: ['e', 'i', 'o', 'u']
print(vowels)
# Result: 'i'
print(vowels.pop(1))
# Result: ['e', 'o', 'u']
print(vowels)

l1 = [10,9,12,3,15]
print(l1.sort(reverse=True))
print(l1)

l2 = ['a','b','c','d','e','f','g','h','i','j']
print( l2[0:2])	
print(l2[0::3])	
print(l2[0:-1])

l2 = ['a','b','c','d','e','f','g','h','i','j']
del l2[3:6]
print(l2)


