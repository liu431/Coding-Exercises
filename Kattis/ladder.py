# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 19:32:01 2018

@author: liu431
"""

import math
n=input().split(" ")
h=int(n[0])
v=int(n[1])
l=h*(1/math.sin(math.radians(v)))
print(math.ceil(l))