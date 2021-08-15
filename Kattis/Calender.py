# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
s=input("").split(' ')

print(s)

a=int(s[0])
b=int(s[1])
c=int(s[2])

if a>31:
    print('Format #3')
elif a>12 and a<=31:
    if c>31:
       print('Format #2')
    else:
       print('Ambiguous')
else:
    if b>12:
       print('Format #1')
    else :
       print('Ambiguous')
      

        

