# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 17:55:48 2018

@author: LI LIU
"""

n=list(input())
wcts=n.count('W')
bcts=n.count('B')
if wcts==bcts:
    print("1")
else:
    print("0")    

#Functional
#print(1 if (lambda t: t[0] == 2 * t[1])((lambda x, c: (len(x), x.count(c)))(input(), 'W')) else 0)
