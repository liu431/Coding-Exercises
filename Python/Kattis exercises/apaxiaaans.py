# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 13:50:59 2018

@author: LI LIU
"""

n=input()
new=""
pre=""
for letter in n:
    if letter!=pre:
        new+=letter
        pre=letter
        
print(new)