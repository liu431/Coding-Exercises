# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 08:59:01 2018

@author: LI LIU
"""
a=dict()

while True:
    inp=input("Name: ")
    if inp=='done': break
    elif inp in a:
        a[inp]+=1
    else:
        a[inp]=1
print(a)