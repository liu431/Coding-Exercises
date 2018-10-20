# -*- coding: utf-8 -*-
"""
Created on Sat Aug 11 09:26:53 2018

@author: LI LIU
"""
D=int(input())
n1=0
n2=0

def sqr(n1,n2):
    while n1<100 and n2<100:
      if (n1+n2)*(n1-n2)==D:
          return n2,n1
          break
      elif (n1+n2)*(n1-n2)>D:
          return sqr(n1,n2+1)
      elif (n1+n2)*(n1-n2)<D :
          return sqr(n1+1,n2)
      else:
          return "impossible"
if sqr(n1,n2) is not None:
    print(*sqr(n1,n2))
   
else:
    print("impossible")
       
    