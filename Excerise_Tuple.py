# -*- coding: utf-8 -*-
"""
Created on Tue May 21 09:47:17 2019

@author: Training28
"""

1.Write a Python program to create a tuple.
x=()
print(x)
b=tuple()
print(tuple)


2.Write a Python program to create a tuple with different data types

b=("tuple",3.213,12,'asd')
print(b)



3.Write a Python program to add an item in a tuple
z=(1,2,3,4,5)
print(z)
y=z+(9,)
print(y)
y=y[:5]+(10,20,30) + y[:5]
print(y)



4.Write a Python program to convert a tuple to a string.
p=('a','b','c')
print (p)
str1=''.join(p)
print(str1)


5.Write a Python program to check whether an element exists within a tuple
p=('a','b','c')
print('a' in p)
print(2 in p)



6.Write a Python program to convert a list to a tuple

a=[10,20,30]
print(a)
y=tuple(a)
print(y)

7.Write a Python program to remove an item from a tuple
p=('a','b','c','d','e','f','g')
p=p[:2]+p[3:]
print(p)   

8.Write a Python program to nd the length of a tuple

print(len(p))
print(max(p))
print(min(p))


9.Write a Python program to convert a tuple to a dictionary
d=((2,'a'),(3,'b'))
print(dict((y,x)for x,y in d))

10.Write a Python program to reverse a tuple
z=reversed(p)
print(tuple(z))
