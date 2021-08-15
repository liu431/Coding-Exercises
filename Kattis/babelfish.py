# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 10:40:26 2018

@author: LI LIU
"""

trans=dict()
while True:
   s=input()
   if s=="":
        break
   else:
      token=s.split(" ")
      fore=token[1]
      orin=token[0]
      trans[fore]=orin

while True:
      try: 
         word=input().rstrip("\n")
         if word in trans:
            res=trans[word]
            print(res)
         else:
            print("eh")
      except EOFError:
           break