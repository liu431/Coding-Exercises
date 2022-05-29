# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 22:44:04 2018

@author: LI LIU
"""

n=int(input())
die=list(map(int,input().split(" ")))
if len(set(die))==1:
    print("none")
else:
    st=set([x for x in die if die.count(x) ==1])
    index=die.index(max(st))+1
    print(index)
