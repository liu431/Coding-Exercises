# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 15:02:54 2018

@author: liu431
"""
x=int(0)
n=int(input())
for _ in range(n):
  p=input()
  b=int(p[-1])
  a=int(p[:-1])
  x=x+a**b
print(x)