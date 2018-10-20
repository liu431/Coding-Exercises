# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 13:59:19 2018

@author: LI LIU
"""

n=int(input())
s=list(map(int,input().split(" ")))
s.sort()
for i in range(1,n+1):
    for j in range(1,n+1):
        for z in range(1,n+1):
            if s[z]-s[j]==1 and s[j]-s[i]==1:
                s[i]=str(s[i])+'-'+str(s[z])
                s.pop(j)
                s.pop(z)
print(' '.join(map(str, s)))                