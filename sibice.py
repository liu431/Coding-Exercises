# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 11:46:42 2018

@author: liu431
"""

import math
m=input("").split()
N=int(m[0])
W=int(m[1])
H=int(m[2])
D=math.sqrt(W**2+H**2)#Diagonal
for i in range(N):
    x=int(input(""))
    if x<=D:
        print("DA")
    else:
        print("NE")