# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import math
for i in range(1000):
  x=input().split(" ")
  r=float(x[0])
  m=int(x[1])
  c=int(x[2])
  if r==0:
      break
  else:
      a1=(r**2)*math.pi
      a2=(c/m)*4*(r**2)
      print(round(a1,5),round(a2,5),sep=" ")
      

