# -*- coding: utf-8 -*-
"""
Created on Sat Jun 30 10:06:11 2018

@author: LI LIU
"""

n=int(input())
for i in range(n):
    inp=input().split(" ")
    ps=inp[1].split("/")
    bn=inp[2].split("/")
    if int(ps[0])>=2010:
        print(inp[0],"eligible")
    elif int(bn[0])>=1991: 
        print(inp[0],"eligible")
    elif int(inp[3])>=41:
        print(inp[0],"ineligible")
    else:
        print(inp[0],"coach petitions")
        
       
