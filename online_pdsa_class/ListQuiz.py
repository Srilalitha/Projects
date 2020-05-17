# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 12:09:54 2020

@author: shanmukha
"""

def f():
    pass
print(type(f()))

print(type(1J))

import re
sentence = 'Learn Python Programming'
test = re.match(r'(.*) (.*?) (.*)', sentence)
print(test.group())

a = [1,2,3,None,(),[],]
print( len(a))

print (abc)

num = '5'*'5'

list1 = [ 'Tech', 404, 3.03, 'Beamers', 33.3 ]
print (list1[1:3])

def a(b, c, d):
   pass

print(a(1,2,3))

tuple1 = (1231, 'griet',[40,90] )
print (tuple1 * 2)

k=3/5
print(type(1/2))

x = True         #False
y = False        #True
z = False        #True
if not x or y:
    print (1)
elif not x or not y and z:
    print( 2)
elif not x or y or not y and x:
    print (3)
else:
    print( 4)

test_list = [1, 5, 5, 5, 5, 1]
max = test_list[0]
indexOfMax = 0
for i in range(1, len(test_list)):
    if test_list[i] > max:
        max = test_list[i]
        indexOfMax = i
print(indexOfMax)



test_list = [1,5,10,19,55,30,55,99]
test_list.pop(5) 
test_list.remove(19)
test_list.remove(55) 
test_list.remove(55)
print(test_list)


test_list.remove(5) 
test_list.remove(19) 
test_list.remove(55)
print(test_list)


for n in range(1, 6, 1):
    print((str(n)+ ' ')*5)
   
    
    
class A:
    def __init__(self):
        self.a = 1
        self.__b = 1
 
    def getY(self):
        return self.__b
    
#    def show(self):
#        print(self.a, self.__b)
        
        
obj = A()
obj.a = 45
print(obj.a)
#print(obj.show())