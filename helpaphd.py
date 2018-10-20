# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 18:14:52 2018

@author: liu431
"""

n=int(input())
for i in range(n):
    m=input()
    if m=='P=NP':
        print("skipped")
    else:
      m=m.split("+")
      a=int(m[0])
      b=int(m[1])
      print(a+b)