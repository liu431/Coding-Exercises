# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 18:26:49 2018

@author: liu431
"""
n=int(input())
for i in range(n):
    m=input().split(" ")
    b=int(m[0])
    p=float(m[1])
    BPM=60*b/p
    ABPM1=60/(p/(b-1))
    ABPM2=60/(p/(b+1))
    print(round(ABPM1,4),round(BPM,4),round(ABPM2,4))