# -*- coding: utf-8 -*-
"""
Created on Thu May 23 20:35:36 2019

@author: Training28
"""
1. Write the syntax for try-finally block.

import sys

randomList = ['a', 0, 2]

for entry in randomList:
    try:
        print("The entry is", entry)
        r = 1/int(entry)
        break
    except:
        print("Oops!",sys.exc_info()[0],"occured.")
        print("Next entry.")
        print()
    finally:
        print("The reciprocal of",entry,"is",r)


2. Write a python program for except clause with exception.

try:
    with open (r'C:\file.log') as file:
        read_date=file.read()
except FileNotFoundError as fnf_error:
    print(fnf_error)

3. Write a python program for except clause with multiple exception.

try:
    y=input('Please enter a number\n')
    print(y)
except (ValueError,TypeError) as a:
    print(type(a),'::',a)
     

4. Write a python program for raising an exception using raise clause.
5. Write a python program for user defined exceptions.
6. Write a python program for custom exceptions.

import random
try:
  ri = random.randint(0, 2)
  if ri == 0:
    infinity = 1/0
  elif ri == 1:
    raise ValueError("Message")
    #raise ValueError, "Message" # Deprecated
  elif ri == 2:
    raise ValueError # Without message
except ZeroDivisionError:
  pass
except ValueError as valerr:
# except ValueError, valerr: # Deprecated?
  print (valerr)
  raise # Raises the exception just caught
except: # Any other exception
  pass
finally: # Optional
  pass # Clean up

class CustomValueError(ValueError): pass # Custom exception
try:
  raise CustomValueError
  raise TypeError
except (ValueError, TypeError): # Value error catches custom, a derived class, as well
  pass                          # A tuple catches multiple exception classes

