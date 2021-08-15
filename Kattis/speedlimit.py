# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 22:47:55 2018

@author: LI LIU
"""
while True:
  n=int(input())
  if n==-1:
     break
  else:
    it=0
    miles=0
    for i in range(n):
       s,t=map(int,input().split())
       t-=it
       it+=t
       miles=miles+s*t

       print(miles,"miles")

