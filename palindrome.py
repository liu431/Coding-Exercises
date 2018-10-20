# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 10:06:34 2018

@author: LI LIU
"""
def pal(word):
    if len(word)<=1:
        return True
    else:
        return word[0]==word[-1] and pal(word[1:-1])
word=input()           
if pal(word)==True:
   print('PALINDROME')
else:
   print('NOT PALINDROME')
