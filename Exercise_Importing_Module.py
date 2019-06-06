# -*- coding: utf-8 -*-
"""
Created on Mon May 20 21:34:24 2019

@author: Training28
"""

1.
Write a Python program to read an entire text le.

def file_read(fname):
    txt = open(fname)
    print(txt.read())

file_read(r'C:\Users\Training28\Anaconda3\test.txt')



2.Write a Python program to read rst n lines of a le.

def file_read_from_head(fname, nlines):
    from itertools import islice
    with open(fname) as f:
        for line in islice(f, nlines):
            print(line)
file_read_from_head(r'C:\Users\Training28\Anaconda3\test.txt',2)



3.Write a Python program to append text to a le and display the text
def file_read(fname):
        from itertools import islice
        with open(fname, "w") as myfile:
                myfile.write("Python Exercises\n")
                myfile.write("Java Exercises")
        txt = open(fname)
        print(txt.read())
file_read(r'test.txt')




4.Write a Python program to read last n lines of a le.
import sys
import os
def file_read_from_tail(fname,lines):
    bufsize = 8192
    fsize = os.stat(fname).st_size
    iter = 0
    with open(fname) as f:
        if bufsize > fsize:
            bufsize = fsize-1
            data = []
            while True:
                iter +=1
                f.seek(fsize-bufsize*iter)
                data.extend(f.readlines())
                if len(data) >= lines or f.tell() == 0:
                    print(''.join(data[-lines:]))
                    break

file_read_from_tail(r'test.txt',2)
