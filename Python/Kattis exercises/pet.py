# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 08:22:32 2018

@author: LI LIU
"""
s=0
for i in range(3):
    m=input().split(" ")
    si=sum(int(i) for i in m) #sum(map(int,m))
    s=max(s,si)
    if s==si:
        index=i+1
print(index,s)
    