# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 22:37:18 2018

@author: LI LIU
"""

#Compare the lenths of two inputs
s = input()
t = input()

if len(s) >= len(t):
    print('go')
else:
    print('no')
    
    
    
l1=input()
cta=0
for char in l1:
    if char=='a':
        cta+=1
        
l2=input()
cta2=0
for char in l2:
    if char=='a':
        cta2+=1
        
if cta2<=cta:
    print('go')
else:
    print('No')