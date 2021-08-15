# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 10:19:44 2018

@author: LI LIU
"""

n=int(input())
for i in range(n):
  test=input().split(" ")
  inf=[]
  m=input()
  while m !='what does the fox say?':
      inf.append(m.split(" ")[2])
      m=input()

  for i in range(len(inf)):   
      while test.count(inf[i])>0:
            test.remove(inf[i])
  print(*test)

   
