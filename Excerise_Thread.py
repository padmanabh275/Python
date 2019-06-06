# -*- coding: utf-8 -*-
"""
Created on Wed May 29 16:15:52 2019

@author: Training28
"""
#There are two different kind of threads −
#kernel thread
#user thread
#Kernel Threads are a part of the operating system, while the User-space threads are not implemented in the kernel.

#There are two modules which support the usage of threads in Python3 −
#_thread this is now being used 
#threading

1.Write a python program using thread.start_new_thread ( function, args[, kwargs] ).

import _thread
import time
import threading
# Def a function for the thread
def print_name(threadName,delay):
    count=0
    while count<5:
        time.sleep(delay)
        count +=1
        print('%s: %s' % (threadName,time.ctime(time.time())))
 #Creating two threads
try:
    _thread.start_new_thread(print_name,('Thread-1',2,))
    _thread.start_new_thread(print_name,('Thread-2',4,))
except:
    print('Error:!')
while 1:
    pass
    

2.Write a python program using threading.activeCount().

threading.active_count()

3.Write a python program using threading.currentThread().

threading.current_thread()

4.Write a python program using threading.enumerate().

threading.enumerate()

5.Write a python program that will block the thread if a lock occurs.
6.Give 5 points under which lock will occur.
7.Write simple program under which re-entrant lock occurs.
8.Write a simple program with semaphores.
