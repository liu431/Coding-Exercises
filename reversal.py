# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 10:26:53 2018

@author: LI LIU
"""

m=input()
def res(m):
    if len(m)==1:
        return m[0]
    else:
        return res(m[1:])+m[0]
    
print(res(m))