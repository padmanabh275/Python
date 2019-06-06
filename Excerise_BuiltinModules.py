# -*- coding: utf-8 -*-
"""
Created on Mon May 20 20:50:31 2019

@author: Training28
"""

1.
Write python program using math.ceil(x), math.copysign(x, y), math.fabs(x)
import math
# returns celing of x as an integral integer >=x
x=-20.12
y=20.25
math.ceil(x) # output would be round only to small no 
math.copysign(x,y)
math.fabs(y) # absolute of float x 



.
2.
Write python program using
class fractions.Fraction(numerator=0, denominator=1)
class fractions.Fraction(other_fraction)
class fractions.Fraction(oat)
class fractions.Fraction(decimal)
class fractions.Fraction(string)

from fractions import Fraction
Fraction(16, -10)
Fraction(123)
Fraction()
Fraction('3/7')
Fraction('1.414213 \t\n')

from decimal import Decimal
Fraction(Decimal('1.1'))
from fractions import Fraction
Fraction('3.1415926535897932').limit_denominator(1000)
from math import pi, cos
Fraction(cos(pi/3))
Fraction(cos(pi/3)).limit_denominator()
from math import floor
floor(Fraction(355, 113))



3.
Write python program using
operator.lt(a, b)
operator.le(a, b)
operator.eq(a, b)
operator.ne(a, b)
operator.ge(a, b)
operator.gt(a, b)
operator.__lt__(a, b)
operator.__le__(a, b)
operator.__eq__(a, b)
operator.__ne__(a, b)
operator.__ge__(a, b)
operator.__gt__(a, b)

import operator

def cmp_fun():
    a, b = 5, 3
    print (operator.lt(a,b))
    #True Same as a<b.
    print (operator.le(a, b))
    # False
    print (operator.eq(a,b))
    # False
    print (operator.ne(a,b))    
    #TRUE
    print(operator.ge(a,b))
    #False Same as a>=b
    print (operator.gt(a, b))
    # True
    print (operator.__lt__(a, b))
    #TRUE
    print (operator.__le__(a, b))
    #TRUE
    print (operator.__ne__(a, b))
    #TRUE Same as a<b.
    print (operator.__ge__(a, b))    
    #FALSE
    print (operator.__gt__(a, b))
    #FALSE
    print (operator.__eq__(a, b))
    #FALSE


4.
Write python program using
itertools.chain(*iterables)
itertools.combinations(iterable, r)
itertools.compress(data, selectors)
itertools.count(start=0, step=1)
itertools.cycle(iterable)
itertools.dropwhile(predicate, iterable)
itertools.groupby(iterable[, key])

import itertools
import operator
shapes = ['circle', 'triangle', 'square',]
result = itertools.combinations(shapes, 2)
for each in result:
    print(each)

for i in itertools.count(10,3):
    print(i)
    if i > 20:
        break    

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'violet']
for color in itertools.cycle(colors):
    print(color)
shapes = ['circle', 'triangle', 'square', 'pentagon']
selections = [True, False, True, False]
result = itertools.compress(shapes, selections)
for each in result:
    print(each)

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]
result = itertools.dropwhile(lambda x: x<5, data)
for each in result:
    print(each)

robots = [{
    'name': 'blaster',
    'faction': 'autobot'
}, {
    'name': 'galvatron',
    'faction': 'decepticon'
}, {
    'name': 'jazz',
    'faction': 'autobot'
}, {
    'name': 'metroplex',
    'faction': 'autobot'
}, {
    'name': 'megatron',
    'faction': 'decepticon'
}, {
    'name': 'starcream',
    'faction': 'decepticon'
}]
for key, group in itertools.groupby(bots, key=lambda x: x['faction']):
    print(key)
    print(list(group))



