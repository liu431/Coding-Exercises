# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 15:42:29 2018

@author: LI LIU
"""

x,c,r=map(int,input().split(" "))
if x<(c-r) or x>(c+r):
    print('False')
else:
    print('True')
    
    
    i=0
tol=0
while i<n:
    xi=int(x[i])
    if xi<0:
        tol+=1
    i+=1
print(tol)