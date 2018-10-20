# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 11:12:55 2018

@author: LI LIU
"""
sens=[]
rag=0
while True:
       sen=input()
       if sen=="":
           break
       senl=len(sen)
       sens.append(senl)

    
n=max(sens)
for i in range(len(sens)-1):
    score=(n-sens[i])**2
    rag+=score
print(rag)