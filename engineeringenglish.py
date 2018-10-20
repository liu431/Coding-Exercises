# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 22:39:44 2018

@author: LI LIU
"""
s = set()

try:
  while True:
    x = ''
    for l in input().split(' '):
      if not l.lower() in s:
        x += l + ' '
        s.add(l)
      else:
        x += '. '
    print(x)
except EOFError:
  pass           