# -*- coding: utf-8 -*-
"""
Created on Sun Jul 29 21:30:28 2018

@author: LI LIU
"""

n=int(input())
tree=list(map(int,input().split(" ")))
tree.sort(reverse=True)
max=0
time=0
for i in range(len(tree)):
    time=tree[i]+i+1
    if time>max:
        max=time
print(max+1)
    