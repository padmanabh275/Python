# -*- coding: utf-8 -*-
"""
Created on Mon May 27 10:46:17 2019

@author: Training28
"""

write a python program for matching a pattern.

import re
patterns=['Software Testing','Padmanabh']
text='Software Testing is fun'
for pattern in patterns:
    print('Looking for "%s" in "%s"->'% (pattern,text),end =' ')
    if re.search(pattern,text):
        print('Match found')
    else:
        print('No Match')


write python program for matching a string.

b='abc@google.com,timepass@hotmail.com,check@yahoomail.com'
emails=re.findall(r'[\w\.-]+@[\w\.-]+',b)
for email in emails :
    print(email)
    

write a python program for matching flags.

ss = """abc
def
ghi"""
#same expression with multiline as flat option
r1 = re.findall(r"^\w", ss)
r2 = re.findall(r"^\w", ss, flags = re.MULTILINE)
print(r1)
print(r2)
## Dot all expression with the gap of new line is displayed 
ss = """once upon a time,
there lived a king"""
r1 = re.findall(r".+", ss)
r2 = re.findall(r".+", ss, re.DOTALL)
print (r1)    # ['once upon a time,', 'there lived a king']
print (r2)   # ['once upon a time,\nthere lived a king']

## Unicode utf8 - flat applicaiton 
x1 = re.search(r"\w+", u"♥αβγ!", re.U)
x2 = re.search(r"\w+", u"♥αβγ!")
if x1:
    print x1.group().encode("utf8") # → 「αβγ」
else:
    print "no match"
print (x2)  

# Verbose Flat

p1 = re.compile(r"""\d +  # the integral part
                   \.    # the decimal point
                   \d *  # some fractional digits""", re.X)

p2 = re.compile(r"\d+\.\d*")    # pattern p2 is same as p1

r1 = re.findall(p1, u"a3.45")
r2 = re.findall(p2, u"a3.45")

print r1[0].encode("utf8")  # 3.45
print r2[0].encode("utf8")  # 3.45


write a python program for searching a string.

string=input('Enter a string')
g=re.search('(ad.*)',string)
if g:
    print('search',g.group(1))
s=re.match('(na.*)',string)
if s:
    print('match',s.group(1))
    

write a python program for searching a pattern.

patterns=['fox','dog','horse']
text='The quick brown fox jumps over the lazy dog.'
for pattern in patterns:
    print('Searching for "%s" in "%s"->' % (pattern,text),)
    if re.search(pattern,text):
        print('Matched')
    else:
        print('Not Matched')


write a python program for searching flags.

m = re.search("b", "ABC")
m is None
m = re.search("b", "ABC", flags=re.IGNORECASE)
m.group()
m = re.search("a.b", "A\nBC", flags=re.IGNORECASE)
m is None
m = re.search("a.b", "A\nBC", flags=re.IGNORECASE|re.DOTALL)
m.group()


write a python program for searching and replacing a string.

items = ["zero", "one", "two"]
output=re.sub(r"a\[([0-3])\]", lambda match: items[int(match.group(1))], "Items: a[0], a[1], something,a[2]")
print(output)

re.sub(r"t([0-9])([0-9])", r"t\2\1", "t13 t19 t81 t25")

re.findall(r"[0-9]{2,3}", "some 1 text 12 is 945 here 4445588899")


write a python program for searching and replacing a pattern.

sentence = "This is a phone number 672-123-456-9910"
pattern = r".*(phone).*?([\d-]+)"
match = re.match(pattern, sentence)
match.groups()
match.group()
match.group(0)
match.group(1)
match.group(2)
match.group(1,2)

write a python program for searching and replacing flags.
## THis library checks for Emojis and replaces it with the regular expressions
from cucco import Cucco
cucco = Cucco()
a=cucco.replace_emojis(':) :)) :( FSDFSDDFSDfv')
print(a)
    
write the syntax and a simple program for regular expression pattern in python.

import re
text = 'You can try to find an ant in this string'
pattern = 'an?\w'
for match in re.finditer(pattern, text):
    sStart = match.start()
    sEnd = match.end()
    sGroup = match.group()
    print('Match "{}" found at: [{},{}]'.format(sGroup, sStart,sEnd))


