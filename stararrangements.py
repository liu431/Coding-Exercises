# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

x=int(input(""))
print(x,":",sep='')
m=2
while m<x:
  if x%(2*m-1)==m or x%(2*m-1)==0:
   print(m,m-1,sep=',')
  if x% m==0:
     print(m,m,sep=',')
  m+=1     
