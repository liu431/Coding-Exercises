# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
x=input().split(" ")
a=x[0]
af=a[2]+a[1]+a[0]
b=x[1]
bf=b[2]+b[1]+b[0]

if int(af)>int(bf):
    n=str(af)
else:
    n=str(bf)
print(n)