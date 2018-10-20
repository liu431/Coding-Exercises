# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 21:59:41 2018

@author: LI LIU
"""

lists = []
n = 10
for i in range(n):
    lists.append([])
lists[0]=[0]
lists[1]=[0,1,2,3,4,5,6,7,8,9]
lists[2]=[0,2,3,5,6,8,9]
lists[3]=[3,6,9]
lists[4]=[0,4,5,6,7,8,9]
lists[5]=[0,5,6,8,9]
lists[6]=[6,9]
lists[7]=[0,7,8,9]
lists[8]=[0,8,9]
lists[9]=[9]

    
def close(dig,ten,t):
    lists[ten].append(dig)
    lists[ten].sort()
    ind=lists[ten].index(dig)
    if ind==0:
        return str(t[:-1])+str(lists[ten][1])
    else:
        if dig>(lists[ten][ind-1]+lists[ten][ind+1])/2:
           return str(t[:-1])+str(lists[ten][ind+1])
        else:
           return str(t[:-1])+str(lists[ten][ind-1])
       
        
k=int(input())
for i in range(k):
    t=input()
    if len(t)==1:
        print(t)
    else:
       ten=int(t[-2])
       dig=int(t[-1])
       if dig in lists[ten]:
          print(t)
       else:
          print(close(dig,ten,t))    
    
    
    
    
    
    
    
    
    
    