# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
n=int(input())
for i in range(n):
    m=input().split(" ")
    a=int(m[0])
    b=int(m[1])
    c=int(m[2])
    if (a-b)==c or (a-b)==-c or (a+b)==c or a*b==c or a/b==c or b/a==c:
       print("possible")
    else:
       print("Impossible")