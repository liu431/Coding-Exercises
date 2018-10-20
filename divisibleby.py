# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 13:03:35 2018

@author: LI LIU
"""

m,n,p,q=map(int,input().split(" "))
sum=0
while m<=n:
    if m%p==0 and m%q==0:
        sum=sum+m
    m+=1
print(sum)