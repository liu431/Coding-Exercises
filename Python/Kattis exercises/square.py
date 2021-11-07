# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 21:31:33 2018

@author: LI LIU
"""
def exp(x,n):
    if n==0:
        return 1
    elif n==1:
        return x
    elif n>1 and n%2==0:
        return exp(x*x,n/2)
    else:
        return x*exp(x*x,(n-1)/2)
    
x,n=map(int,input().split(" "))
print(exp(x,n))