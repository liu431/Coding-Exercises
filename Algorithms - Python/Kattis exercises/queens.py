# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 14:38:10 2018

@author: LI LIU
"""
def digtest(l1,l2):

    for i in range(a) and j in range(a):
        if l2[i]-l2[j]==l1[i]-l1[j] or l2[i]-l2[j]==-l1[i]+l1[j]:
            return True
        
    
    
a=int(input())
l1=[]
l2=[]
for i in range (a):
    pos=input().split(" ")
    x=int(pos[0])
    y=int(pos[1])
    l1.append(x)
    l2.append(y)
    if x is in l1 or y is in l2:




if len(l1)!=len(set(l1)) or len(l2)!=len(set(l2)) or digtest(l1,l2):
    print("incorrect")
    
else:
   print("correct")
