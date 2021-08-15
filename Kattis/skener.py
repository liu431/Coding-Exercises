# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 15:27:46 2018

@author: liu431
"""

m=input().split(" ")
R=int(m[0])
C=int(m[1])
Zr=int(m[2])
Zc=int(m[3])
for i in range(R):
    x=input()
    out=""
    for j in range(C):
        out+=x[j]*Zc
    for k in range (Zr):
        print(out)
        
