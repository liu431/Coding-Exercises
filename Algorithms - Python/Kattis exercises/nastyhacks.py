# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
n=int(input())#n cases
for i in range(n):
  m=input().split(" ")
  r=int(m[0])
  e=int(m[1])
  c=int(m[2])
  diff=e-r-c
  if diff>0:
      print("advertise")
  if diff==0:
      print("does not matter")
  if diff<0:
      print("do not advertise")    
   