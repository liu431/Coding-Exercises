# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 12:48:13 2018

@author: LI LIU
"""

def mccarthy(n):
    if n>100:
        return n-10
    else:
        return mccarthy(mccarthy(n+11))
    
n=int(input())
print(mccarthy(n))