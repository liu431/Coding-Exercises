# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 22:12:19 2018

@author: LI LIU
"""
try:
    
    while True:
      line=input()
      m,n=map(int,line.split(" "))
      ans=abs(m-n)
      print(ans)
    
except EOFError:
    pass
