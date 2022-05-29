# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 09:27:49 2018

@author: LI LIU
"""

xcor=[]
ycor=[]
n=int(input())
for i in range(n):
    inp=input().split(" ")
    xcor.append(int(inp[0]))
    ycor.append(int(inp[1]))

for i in range(len(xcor)):
    for j in range (len(xcor)):
      if abs(xcor[j]-xcor[i])==1 and abs(ycor[j]-ycor[i])==1:
        ans="INCORRECT"
      elif xcor[j]==xcor[i] and ycor[j]!=ycor[i]:
        ans="INCORRECT"
      elif ycor[j]==ycor[i] and xcor[j]!=xcor[i]:
        ans="INCORRECT"   
      else:
        ans="CORRECT"
        
print(ans)