# -*- coding: utf-8 -*-
"""
Created on Fri May 24 09:02:39 2019

@author: Training28
"""

1. Write a Python code to import NumPy.

import numpy as np



2. Write a Python program to create 3x3 matrix with values ranging from 5 to 13.

ab=np.arange(5,14).reshape(3,3)
print(ab)


3. Write a Python program to create a null vector of size 10 and update sixth value to 11.

a=np.zeros(10)
a[5]=11
print(a)


4. Write a Python program to create a array with values ranging from 12 to 38.

ac=np.arange(12,39)
print(ac)

6. Write a Python program to reverse an array so that first element becomes last.

reversed=ac[::-1]
print(reversed)

7. Write a Python program to an array converted to a float type.

y=ac.astype(np.float)
type(y)
print(y)

8. Write a Python program to create a 2d array with 1 on the border and 0 inside.

border=np.zeros((5,5))
print(border)
inside=np.pad(border, pad_width=1, mode='constant', constant_values=1)
print(inside)

9. Write a Python program to create a 8x8 matrix and fill it with a checkerboard pattern.
x=np.ones((3,3))
x=np.zeros((8,8),dtype=int)
#odd rows even columns
x[1::2,::2]=1
#even rows odd columns
x[::2,1::2]=1    
print(x)

10. Write a Python program to convert a list and tuple into arrays.

a=[1,2,3]
b=(1,2,3)
c=np.asarray(a)
print(c)
type(c)
d=np.asarray(b)
print(d)
type(d)

11. Write a Python program to append values to the end of an array.

a=np.append(a,[[2,3]])
print(a)

12. Write a Python program to create an empty and a full array.

a=np.empty((3,4))
print(a)
y=np.full((3,4),0)
print(y)

13. Write a Python program to convert the values of Centigrade degrees into Fahrenheit degrees. Centigrade values are stored into a NumPy array.
centigrate=[0, 12, 45.21, 34, 99.91]
values=np.array(centigrate)
print(values)
type(values)
print('The value in centigrade degrees:')
print(5*values/9 - 5*32/9)


14. Write a Python program to find the real and imaginary parts of an array of complex numbers.
x = np.sqrt([1+0j])
y = np.sqrt([0+1j])
print(x.real)
print(y.real)
print(x.imag)
print(y.imag)


15. Write a Python program to test whether each element of a 1-D array is also present in a second array.
a1=np.array([1,2,3,4,5])
a2=np.array([1,2,2])
print(np.isin(a1,a2))


16. Write a Python program to find common values between two arrays.
print(np.intersect1d(a1, a2))


17. Write a Python program to get the unique elements of an array.

print(np.unique(a2))


18. Write a Python program to test if all elements in an array evaluate to True.

# 0 evaluates to false in python 
print(np.all([10, 20, 0, -50]))


19. Write a Python program to test whether any array element along a given axis evaluates to True.
#checks for all elements in an array to be same and then responds the value
print(np.any([10, 20, 0, -50]))


20. Write a Python program to repeat elements of an array.
a=np.repeat(3,4)
print(a)
ab=np.array([[1,0],[1,3]])
print(np.repeat(ab,3))

21. Write a Python program to find the indices of the maximum and minimum values along the given axis of an array.
check=np.array([1,2,3,5,6,7,8,9])
print('max indicies',np.argmax(check))
print('min indicies',np.argmin(check))


22. Write a Python program compare two arrays using numpy.

a=np.array([1,2,3,4,5])
b=np.array([1,2])
print(np.array_equal(a,b))
print(np.array_equiv(a,b))
print(np.allclose(a,b))

23. Write a Python program to save a NumPy array to a text file.
a=np.array([1,2,3,4,5])
b=np.arange(1.0,2.0,22.3)
np.savetxt('file.out',a,delimiter=',')
np.savetxt('text.csv',b,delimiter=',')

24. Write a Python program to create a contiguous flattened array.
a=np.array([[12,12,3],[23,232,23],[232,21,32]])
b=np.ravel(a)
print(b)

25.Write a program to perform addition,minimum and maximum values from a 3D array.
arr = np.arange(36).reshape(3, 4, 3)
print(arr)
print("\nSum of arr : ", np.sum(arr))  
print("Sum of arr(axis = 0) : ", np.sum(arr, axis = 0))  
print("Sum of arr(axis = 1) : ", np.sum(arr, axis = 1)) 
print("Sum of arr(axis = 1) : ", np.sum(arr, axis = 2)) 
  
print("\nSum of arr (keepdimension is True): \n", 
      np.sum(arr, axis = 1, keepdims = True)) 

print('minimum',np.min(arr))
print('max value',np.max(arr))
