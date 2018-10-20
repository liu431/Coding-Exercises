# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 21:24:43 2018

@author: liu431
"""

n=int(input("\n"))
i=0
while i<n:
  x=int(input(""))
  if x % 2==0:
    print(x,"is even")
  else:
    print(x,"is odd")
  i+=1
