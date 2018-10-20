# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 22:32:14 2018

@author: liu431
"""

price=input("").split(" ")
A=int(price[0])
B=int(price[1])
C=int(price[2])

truck1=input("").split(" ")
a1=int(truck1[0])
b1=int(truck1[1])

truck2=input("").split(" ")
a2=int(truck2[0])
b2=int(truck2[1])

truck3=input("").split(" ")
a3=int(truck3[0])
b3=int(truck3[1])

cost=-A*(a1-b1+a2-b2+a3-b3)

if a2<b1:
    cost=cost-2*(A-B)*(b1-a2)
else:
    cost=cost







