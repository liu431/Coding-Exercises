# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 14:50:35 2018

@author: LI LIU
"""
lowC=0
uppC=0
whiC=0
symC=0
a=input()
N=len(a)
for c in a:
    if c.islower()==True:
        lowC+=1
    elif c.isupper()==True:
        uppC+=1
    elif c=='_':
        whiC+=1
    else:
        symC+=1
print(whiC/N)
print(lowC/N)
print(uppC/N)        
print(symC/N)             
        

        
        