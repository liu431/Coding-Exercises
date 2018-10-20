# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 10:12:15 2018

@author: LI LIU
"""
n=int(input())
p1=input().split(" ")
p2=input().split(" ")
def rank(m):
    m=[11 if x=='J' else x for x in m]
    m=[12 if x=='Q' else x for x in m]
    m=[13 if x=='K' else x for x in m]
    m=[14 if x=='A' else x for x in m]
    return m
p1=list(map(int,rank(p1)))
p2=list(map(int,rank(p2)))
res=[]
for i in range(n):
    if p1[i]>p2[i]:
        res.append(1)
    elif p1[i]<p2[i]:
        res.append(-1)
    else:
        res.append(0)
        
pts=sum(res)
if pts>0:
    print('PLAYER 1 WINS')
elif pts<0:
    print('PLAYER 2 WINS')    
else:
    print('TIE')
        