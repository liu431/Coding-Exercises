# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 15:47:26 2018

@author: LI LIU
"""

n1=float(input())
n2=int(input())
tot=0

for i in range(n2):
    #area=input().split(" ")
    #l=float(area[0])
    #w=float(area[1])
    l,w=map(float,input().split())
    tot=tot+(l*w*n1)
print(tot)