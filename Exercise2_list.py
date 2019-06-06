# -*- coding: utf-8 -*-
"""
Created on Mon May 20 19:30:29 2019

@author: Training28
"""

1.Write a Python program to sum all the items in a list.

def sum_all(str1):
    total_sum=0 
    for x in str1:
        total_sum +=x
    return total_sum
print(sum_all([1,2,-3]))

2.Write a Python program to multiplies all the items in a list.
def multiply(str1):
    tot = 1
    for x in str1:
        tot *= x
    return tot
print(multiply([1,2,10]))


3.Write a Python program to get the largest number from a list.

def max_list(list):
    max = list[ 0 ]
    for x in list :
        if x > max:
            max=x
    return max
print(max_list([1,2,10,-8]))


4.Write a Python program to get the smallest number from a list

def min_list(list):
    min = list[ 0 ]
    for x in list :
        if x < min:
            min=x
    return min
print(min_list([1,2,10,-8]))



5.Write a Python program to remove duplicates from a list.

a=[10,20,30,20,10,40,90,80,20,10]
dup_items=set()
unique_items=[]
for x in a:
    if x not in dup_items:
        unique_items.append(x)
        dup_items.add(x)
        
        
print(dup_items)         


6.Write a Python program to check a list is empty or not.

a=[]
if not a:
    print ('This list is empty')



7.Write a Python program to clone or copy a list.

org_list=[10,22,4353,32,1]
new_list=list(org_list)
print(org_list)
print(new_list)

8.Write a Python program to print a specied list after removing the 0th, 4th and
5th elements.
Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
Expected Output : ['Green', 'White', 'Black']

colo=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
colo = [x for (i,x) in enumerate(colo) if i not in (0,4,5)]
print(colo)



9.Write a Python program to get the difference between the two lists.

list1=[1,2,3,4]
list2=[1,2]
print(list(set(list1)-set(list2)))


10.Write a Python program to nd all the values in a list are greater than a specied number.

list1 = [120, 320, 500]
list2 = [12, 17, 21]
print(all(x >= 200 for x in list1))
print(all(x >= 25 for x in list2))





11.Write a Python program to nd a tuple, the smallest second index value from a
list of tuples.

x = [(4, 2), (3, 2), (6, 1)]
print(min(x, key=lambda n: (n[1], -n[0])))



12.Write a Python program to check if the n-th element exists in a given list

a=[1,2,3,4,5,6]
alen=len(a)-1
print(a[alen])



13.Write a Python program to replace the last element in a list with another list.

a=[1,2,3,4,5]
b=[2,3,4]
a[-1:]=b
print(a)




14.Write a Python program to check if all items of a list is equal to a given string

a=['boot','brush','eat','sleep']
b=['brush']
print(all(c=='brush' for c in a))
print(all(c=='brush' for c in b))


15.Write a Python program to convert a string to a list

def convert(string):
    a=list(string.split(' '))
    return a
print(convert('asgffg sda '))


16.Write a Python program to concatenate elements of a list
a=['boot','brush','eat','sleep']
print('-'.join(a))
print(''.join(a))

17.Write a Python program to create multiple lists
obj = {}
for i in range(1, 21):
    obj[str(i)] = []
print(obj)



18.Write a Python program to nd common items from two lists

print(set(a) & set(b))


19.Write a Python program to generate all sublists of a list

from itertools import combinations
def sub_lists(my_list):
	subs = []
	for i in range(0, len(my_list)+1):
	  temp = [list(x) for x in combinations(my_list, i)]
	  if len(temp)>0:
	    subs.extend(temp)
	return subs


l1 = [10, 20, 30, 40]
l2 = ['X', 'Y', 'Z']
print("Original list:")
print(l1)
print("S")
print(sub_lists(l1))
print("Sublists of the said list:")
print(sub_lists(l1))
print("\nOriginal list:")
print(l2)
print("Sublists of the said list:")
print(sub_lists(l2))

20.Write a Python program to get unique values from a list

print("Original List : ",unique_items)
my_set = set(unique_items)
my_new_list = list(my_set)
print("List of unique numbers : ",my_new_list)
