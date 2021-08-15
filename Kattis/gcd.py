# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 10:07:11 2018

@author: LI LIU
"""

def gcd(a,b):
    if a==b:
        print(a)
    elif a>b:
        gcd(a-b,b)
    else:
        gcd(a,b-a)

m=input()
a,b=map(int,m.split(" "))
gcd(a,b)