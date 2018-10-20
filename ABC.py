# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 09:45:15 2018

@author: LI LIU
"""

n=input().split(" ")
n.sort(key=int)
m=list(input())
for i in range(len(m)):
    if m[i]=='A':m[i]='0'
    elif m[i]=='B':m[i]='1'
    elif m[i]=='C':m[i]='2'
    
print('Hello',n[int(m[0])],n[int(m[1])],n[int(m[2])])
    