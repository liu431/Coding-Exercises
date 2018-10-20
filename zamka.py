# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 20:40:44 2018

@author: liu431
"""

L=int(input("")) 
D=int(input("")) #L<=D
X=int(input("")) #1-36
n=L
m=D
def digit_sum(n):
    num_str = str(n)
    sum = 0
    for i in range(0, len(num_str)):
        sum += int(num_str[i])
    return sum

while n<=D:
    if digit_sum(n)==X:
        print(n)
        break
    else:
        n+=1


while m>=L:
    if digit_sum(m)==X:
        print(m)
        break
    else:
        m-=1
        