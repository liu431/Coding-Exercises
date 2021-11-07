# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 21:31:10 2018

@author: LI LIU
"""

n=int(input())
for i in range(n):
    line=input().split(" ")
    if len(line)<2:
        print()
    else:
      if line[0]=='simon' and line[1]=='says':
        print(*line[2:])
      else:
        print()
    