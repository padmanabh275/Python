# -*- coding: utf-8 -*-
"""
Created on Tue May 21 10:08:28 2019

@author: Training28
"""

print(abs.__doc__)

1.Write a python program to create a Dictionary.
my_dict{}
my_dict={1:'Apple',2:'Banana'}
print(my_dict)


2.Write a python program to access the values in the Dictionary.
my_dict={'name':'padmanabh','age':22}

print(my_dict['name'])
print(my_dict.get('age'))

3.Write a python program to update the above created dictionary.

my_dict['age']=30
print(my_dict)

4.Write a python program to delete the above created dictionary.

del my_dict

5.Write a python code to copy the entire dictionary into a new dictionary.
my_dict={'name':'padmanabh','age':22}
my_dict2=my_dict.copy()



6.Write a python code to delete keys from the dictionary.

dict.keys(my_dict)
my_dict.pop('age', None)

print(my_dict)

7.Write a python code to sort the elements in the dictionary.
print(sorted(my_dict))
