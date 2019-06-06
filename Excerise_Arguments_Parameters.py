# -*- coding: utf-8 -*-
"""
Created on Fri May 24 17:50:15 2019

@author: Training28
"""

1.List the scope of variables in python.
variable is something that may change often in your program. First, you use variables to refer to various kinds of data such string, integer, list, etc
Then you manipulate this data through variables.
Global and local 
bulitin 
enclosing 




2.Write the difference between local and global variables.
# Global scope

x = 0

def outer():
    # Enclosed scope
    x = 1
    def inner():
        # Local scope
        x = 2


3.Where does the scope of the following program lies.
def f():
    print s
 s = "I love Geeksforgeeks"
f()

## This throws an error but, it is a local variable


4.Write a program using Lambda in python.
add = lambda x, y : x + y 
print(add(1,2))

5.Write python program using Positional parameters or required parameters or
#Parameters are variables that are given arguments (values).
#Short answer:  A positional argument is any argument that's not supplied as a key=value pair.
def foo(a,b):
    return a+b
foo(1,3)
# a and b are my parameters while 1 and 3 are arguments for a given call to that function.
def hello(first_name, last_name=None):
    print "Hello " + first_name


6.Write python program using positional only

def pos_only_arg(arg, '/'):
    print(arg)
def add_to_queue(items: Union[QueueItem, List[QueueItem]]):
    
    
7.Write python program using Keyword Parameters or default parameters

def product(*numbers, initial=1):
    total = initial
    for n in numbers:
        total *= n
    return total
print('total',(product(1,5,2,3,initial=2)))
print('total',(product(1,5,2,3)))

8.Write python program using variable length positional parameter
def display(*name, **address):
  for items in name:
    print (items)

  for items in address.items():
    print (items)

display('john','Mary','Nina',John='LA',Mary='NY',Nina='DC')

9.Write python program using Variable length keyword parameter
def adder(*num):
    sum = 0
    
    for n in num:
        sum = sum + n

    print("Sum:",sum)
adder(10,2,1)    

10.Write python program using keyword parameter

def print_name(name1, name2):
    print (name1 + " and " + name2 + " are friends")
print_name(name2 = 'John',name1 = 'Gary')  

  
  
 11.Write a program for command line arguments in python
 
import sys

print ('Number of arguments:', len(sys.argv), 'arguments.')
print ('Argument List:', str(sys.argv))
#in command line use the folloiwing command  python test.py (have saved the file seperately in folder)
#python test.py arg1 arg2 arg3 arg4 - output No of arguments - 4 , argument list - etc

 