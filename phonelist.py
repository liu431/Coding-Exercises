# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 10:25:02 2018

@author: LI LIU
"""

t=int(input())
for i in range(t):
    n=int(input())
    nums=sorted([input() for _ in range(n)],key=len,reverse=True)
    d=set()
    ok=True
    for num in nums:
        if not ok:
           continue
        if num in d:
            ok=False
            continue
        for i in range(1,len(num)+1):
            d.add(num[:i])
    print('YES' if ok else 'NO')
 
            