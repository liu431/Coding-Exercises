# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 09:36:17 2018

@author: LI LIU
"""

def negate(m):
    for i in range(len(m)):
        m[i] = -m[i]
    return m
        
n=int(input())
if n==0:
    print ("EMPTY")
else:
    m=input().split(" ")
    m = list(map(int, m))
    print(*negate(m))
    
#Alternative    
mylist = [ 1, 2, 3, -7]
myneglist = [ -x for x in mylist]
print(myneglist)