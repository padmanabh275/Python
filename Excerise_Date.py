# -*- coding: utf-8 -*-
"""
Created on Wed May 22 10:08:51 2019

@author: Training28
"""
import time
import calendar
import datetime


Write a Python script to display the
a) Current date and time 
print('Current Date and Time',datetime.datetime.now())
b) Current year
print('Current Year',datetime.date.today().strftime('%Y'))
c) Month of year
print('Month of Year',datetime.date.today().strftime('%B'))
d) Week number of the year
print('Week No of the year',datetime.date.today().strftime('%W'))
e) Weekday of the week
print('Weekday of the week',datetime.date.today().strftime('%w'))
f) Day of year
print('Day of Year',datetime.date.today().strftime('%j'))
g) Day of the month
print('Day of the month',datetime.date.today().strftime('%d'))
h) Day of week
print('Day of week',datetime.date.today().strftime('%A'))

2. Write a Python program to determine whether a given year is a leap year.
calendar.isleap(2019)

3.Write a Python program to convert a string to datetime.

c=datetime.strptime('May 22 2019 10:57AM', '%b %d %Y %I:%M%p')
print(c)

4.Write a Python program to get the current time in Python.
print(datetime.datetime.now().time())

5.Write a Python program to subtract five days from current date.
from datetime import date, timedelta
date1 = date.today() - timedelta(5)
print('Current Date :',date.today())
print('5 days before Current Date :',date1)



6. Write a Python program to convert unix timestamp string to readable date.

import datetime
datetime.datetime.fromtimestamp.
print(
    datetime.datetime.fromtimestamp(
        int("4020302121")
    ).strftime('%Y-%m-%d %H:%M:%S')
)


7.Write a Python program to print yesterday, today, tomorrow.

import datetime 
today = datetime.date.today()
yesterday = today - datetime.timedelta(days = 1)
tomorrow = today + datetime.timedelta(days = 1) 
print('Yesterday : ',yesterday)
print('Today : ',today)
print('Tomorrow : ',tomorrow)


8. Write a Python program to convert the date to datetime (midnight of the
date) in Python
from datetime import date
from datetime import datetime
date1 = date.today()
print(datetime.combine(date1, datetime.min.time()))

9. Write a Python program to print next 5 days starting from today.

from datetime import date, timedelta
date1 = date.today() + timedelta(5)
print('Current Date :',date.today())
print('5 days after Current Date :',date1)


10. Write a Python program to add 5 seconds with the current time

import datetime
x= datetime.datetime.now()
y = x + datetime.timedelta(0,5)
print(x.time())
print(y.time())


11. Write a Python program to convert Year/Month/Day to Day of Year in
Python.

import datetime
today = datetime.datetime.now()
day_of_year = (today - datetime.datetime(today.year, 1, 1)).days + 1
print(day_of_year)


12. Write a Python program to get current time in milliseconds in Python

import time
milli_sec = int(round(time.time() * 1000))
print(milli_sec)


13. Write a Python program to get week number.
import datetime
print(datetime.date(2019,5,22).isocalendar()[1])

14. Write a Python program to find the date of the first Monday of a given week
import time
print(time.asctime(time.strptime('2019 22 5','%Y %W %w')))

15. Write a Python program to select all the Sundays of a specified year.
from datetime import date,timedelta

def sundays1(year):
    date1=date(year,1,1)
    date1 +=timedelta(days=6-date1.weekday())
    while date1.year==year:
        yield date1
        date1 +=timedelta(days=7)

for s in sundays1(2020):
    print(s)


16. Write a Python program to get days between two dates

from datetime import date
a = date(2019,5,22)
b = date(2019,5,30)
print(b-a)


17.Write a Python program to get the date of the last Tuesday.
from datetime import date
from datetime import timedelta
today=date.today()
lasttue=(today.weekday()-1)% 7 
last_tue=today-timedelta(days=lasttue)
print(last_tue)    

18.Write a Python program to get the last day of a specified year and month

import calendar
year=2019
month=5
print(calendar.monthrange(year,month)[1])


19.Write a Python program to get the number of days of a given month and year.

from calendar import monthrange
year=2019
month=6
print(monthrange(year,month))


20.Write a Python program to convert a date to the timestamp.
import time
import datetime
a=datetime.datetime.now()
print(time.mktime(a.timetuple()))

21.Write a Python program to convert a string date to the timestamp.

import time
import datetime
a='22/05/2019'
print(time.mktime(datetime.datetime.strptime(a,'%d/%m/%Y').timetuple()))


22.Write a Python program to convert two date difference in days, hours,
minutes, seconds.

from datetime import datetime,time

def diff_in_sec(date1,date2):
    timedelta=date2-date1
    return timedelta.days * 24*3600 + timedelta.seconds

def diff_in_sec1(seconds):
	minutes, seconds = divmod(seconds, 60)
	hours, minutes = divmod(minutes, 60)
	days, hours = divmod(hours, 24)
	return (days, hours, minutes, seconds)


da1=datetime.strptime('2019-05-22 01:00:00','%Y-%m-%d %H:%M:%S')
da2=datetime.now()
print('\n %d days,%d hours,%d minutes ,%d seconds' %diff_in_sec1(diff_in_sec(da2,da1)))



