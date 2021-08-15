# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 18:40:08 2018

@author: liu431
"""

m=input()
n=len(m)
c1=0#T
c2=0#C
c3=0#G
pts=0
for i in range(n):
    if m[i]=='T':
       c1+=1
    if m[i]=='C':
       c2+=1   
    if m[i]=='G':
       c3+=1
pts=c1**2+c2**2+c3**2
pts=pts+min(c1,c2,c3)*7
print(pts)







       