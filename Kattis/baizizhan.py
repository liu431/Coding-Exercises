# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 14:49:14 2018

@author: LI LIU
"""
def distance(w1,w2,m,n):
    if m==0:
        return n
    if n==0:
        return m
    if w1[m-1]==w2[n-1]:
        return distance(w1,w2,m-1,n-1)
    return 1+min(distance(w1,w2,m,n-1),distance(w1,w2,m-1,n),distance(w1,w2,m-1,n-1))                
                 
              
k=int(input())
for i in range(k):
    w1=list(input())
    w2=list(input())
    m=len(w1)
    n=len(w2)
    step=distance(w1,w2,m,n)
    print(step)
            
