# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 15:54:25 2018

@author: LI LIU
"""

A=list(map(int,input().split(" ")))
A.sort(reverse=True)
length=len(A)
mult=A[0]*A[1]*A[2]
mult2=A[0]*A[length-1]*A[length-2]
print(max(mult,mult2))
