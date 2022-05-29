# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

n=input().split("-")
k=len(n)
SV=""
for i in range(k):
    n1=n[i]
    SV+=n1[0]
    i+=1
print(SV)