# -*- coding: utf-8 -*-
"""
Created on Mon May 20 15:44:03 2019

@author: Training28
"""

def series(n):
    for i in range(0,n):
        for j in range(0,i+1):
            print ('*',end='')
        print ('\r')

for i in [1,2,3,4,5]:
    if i==3:
        pass
    print ("Pass the value",i)
print (i)


def words(n,str):
    word_len=[]
    txt=str.split(' ')
    for x in txt:
        if len(x)>n:
            word_len.append(x)
    return word_len
print(words(3,'this is the trial of the version'))    




1.Write a Python program to calculate the length of a string.
name='padmanabh'
len(name)
2.Write a Python program to count the number of characters (character frequency) in a string.
def charc_count(str1):
    dict={}
    for n in str1:
        keys=dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] =1
    return dict
print (charc_count('sdasdasasabh'))

 OPTION 2
from collections import Counter
print(Counter('cats on wheels'))

OPTION 3
word = input('Learn how to write ')

Alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

for i in range(0,26): 
    print(word.count(Alphabet[i]))


3.Write a Python program to get a string made of the rst 2 and the last 2 chars from a given a
string. If the string length is less than 2, return instead of the empty string

name='s'
if len(name)==0:
    print('empty stirng')
else:
    print(name[:2])
    print(name[-2:])


4.Write a Python program to get a string from a given string where all occurrences of its rst
char have been changed to '$', except the rst char itself.
def change_char(str1):
  char = str1[0]
  str1 = str1.replace(char, '$')
  str1 = char + str1[1:]

  return str1

print(change_char('adsdsaaaaddd'))




5.Write a Python program to get a single string from two given strings, separated by a space and
swap the rst two characters of each string.

def mixup(a,b):
    new_a=b[:2]+a[2:]
    new_b=a[:2]+b[2:]
    return new_a + ' '+ new_b
print(mixup('abc','zew'))

6.Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If
the given string already ends with 'ing' then add 'ly' instead. If the string length of the given
string is less than 3, leave it unchanged

def ing(str1):
    length=len(str1)
    if length>2:
        if str1[-3:]=='ing':
            str1 +='ly'
        else:
            str1 +='ing'
    return str1
print(ing('ab'))
print(ing('abc'))
print(ing('deputie'))

7.Write a Python program to nd the rst appearance of the substring 'not' and 'poor' from a
given string, if 'bad' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'.
Return the resulting string

def poor(str1):
    s_not=str1.find('not')
    s_poor=str1.find('poor')
    if s_poor>s_not and s_not>0 and s_poor>0:
        str1=str1.replace(str1[s_not:(s_poor+4)],'good')
        return str1
    else:
        return str1

print(poor('The lyrics is not that poor!'))
print(poor('The lyrics is poor!'))



8.Write a Python function that takes a list of words and returns the length of the longest one

def longwords (words_list):
    word_len=[]
    for n in words_list:
        word_len.append((len(n),n))
    word_len.sort()
    return word_len[-1][1]
print(longwords(["this", "is", "it", "the", "longest", "word", "in", "the", "alphabet"]))    


9.Write a Python program to remove the nth index character from a nonempty string
def remove_char(str, n):
      first_part = str[:n] 
      last_part = str[n+1:]
      return first_part + last_part
print(remove_char('asdasdasd',3))

10.Write a Python program to change a given string to a new string where the rst and last chars
have been exchanged

def char_exchange(str1):
    return str1[-1:]+str1[1:-1]+str1[:1]
print(char_exchange('abcd'))
print(char_exchange('123454'))


11.Write a Python program to remove the characters which have odd index values of a given
string.

def odd_remove(str1):
    result=""
    for i in range(len(str1)):
        if i%2==0:
            result=result +str1[i]
    return result 
print (odd_remove ('abcded'))


12.Write a Python program to count the occurrences of each word in a given sentence

def occurances(str1):
    a=dict()
    b=str.split()
    for x in b:
        if x in a:
            a[x] +=1
        else:
            a[x]=1
    return a

print (occurances('This is the first trial'))

13.Write a Python script that takes input from the user and displays that input back in upper and
lower cases

def user_request(str1):
    req_input=input('What is your name')
    print('Your Name',req_input.upper())
    print('Your name',req_input.lower())
  
print(user_request('asdassa'))



14.Write a Python program that accepts a comma separated sequence of words as input and
prints the unique words in sorted form (alphanumerically).

req_input=input('input comma seperate values')
words=[word for word in req_input.split(',')]
print(' '.join(sorted(list(set(words)))))


15.Write a Python function to create the HTML string with tags around the word(s).

def tags(tag,word):
    return '<%s>%s</s%s>' %(tag,word,tag)
print (tags('i','python'))


16.Write a Python function to insert a string in the middle of a string.

def middle_string(str1,word):
    return str1[:2] + word + str1[2:]
    
print (middle_string('[[]]','fdfffff'))


17.Write a Python function to get a string made of 4 copies of the last two characters of a
specied string (length must be at least 2)

def last2(str1):
    sub_str=str1[-2:]
    return sub_str*4
print (last2('quick'))




18.Write a Python function to reverses a string if it's length is a multiple of 4

def reverse(str1):
    if len(str1) % 4 ==0:
        return ''.join(reversed(str1))
    return str1
print(reverse('abcd'))


19.Write a Python function to convert a given string to all uppercase if it contains at least 2
uppercase characters in the rst 4 characters.

def trial_case(str1):
    a=0
    for z in str1[:4]:
        if z.upper()==z:
            a=a+1
        if z >= 2:
            return str1.upper()
        return str1
print(trial_case('Trial'))




20.Write a Python program to check whether a string starts with specied characters

abc='asdasdas'
print(abc.startswith('asd'))

              