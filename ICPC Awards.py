# -*- coding: utf-8 -*-
"""
Created on Wed May 30 07:45:53 2018

@author: LI LIU
"""

k=int(input())
list=[]
for i in range(k):
    n=input().split(" ")
    uni=str(n[0])
    team=str(n[1])
    if uni in list:
        pass
    else:
        list.append(uni)
        if len(list)<=12:
           print(uni,team)
        
    
