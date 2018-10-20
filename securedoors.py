# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 15:16:50 2018

@author: LI LIU
"""

n=int(input())
inside=[]
for i in range(n):
    cmd=input().split(" ")
    act=cmd[0]
    name=cmd[1]
    if act=='entry':
       if name in inside:
          print(name+" "+"entered (ANOMALY)")
       else:
          inside.append(name)
          print(name+" "+"entered")
          
    else:
        if name in inside:
           inside.remove(name)
           print(name+" "+"exited")
        else:
           print(name+" "+"exited (ANOMALY)")
          

    
