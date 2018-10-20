# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 09:20:00 2018

@author: LI LIU
"""
from itertools import permutations
x0,y0,x1,y1=map(int,input().split(" "))

def path(x0,y0,x1,y1):
    way=[]
    while x1>x0:
        way.append("right")
        x0+=1
    while x1<x0:
        way.append("left")
        x0-=1
    while y1>y0:
        way.append("up")
        y0+=1
    while x1<x0:
        way.append("down")
        y0-=1 
    return way
way=path(x0,y0,x1,y1)
perm=permutations(way)
for i in list(set(perm)):
    print(*i if len(way)!=0 else "NONE" )
        