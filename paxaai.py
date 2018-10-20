# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 15:07:54 2018

@author: LI LIU
"""

def res(m):
    i=0
    n=len(m)
    if n%2==0:
        while i <= n-1:
           m[i],m[i+1]=m[i+1],m[i]
           i=i+2
        return m  
    
    else:
         while i <= n-2:
           m[i],m[i+1]=m[i+1],m[i]
           i=i+2
         return m 

m=list(input())
print("".join(res(m)))