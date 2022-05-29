# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 15:36:58 2018

@author: liu431
"""

z=input("").split(" ")
first=z[0]
last=z[1]
c=int(len(last))
if c==5:
   print(first,last*4)
else:
    print(first,last*c)
