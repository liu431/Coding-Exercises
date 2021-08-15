# -*- coding: utf-8 -*-
"""
Created on Sun Jul  8 11:40:51 2018

@author: LI LIU
"""

n=int(input())
ct=0
if n==0:
    print(ct)
else:
   m=input().split(" ")

   for i in range(n):
      if int(m[i])<0:
          ct+=1
   print(ct) 