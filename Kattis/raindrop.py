# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 15:32:19 2018

@author: LI LIU
"""

n=int(input())
me=list(map(int,input().split(" ")))
pos=[x for x in me if x>0]
print("INSUFFICIENT DATA" if len(pos)==0 else int(sum(pos)/len(pos)))
