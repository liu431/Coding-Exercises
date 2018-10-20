# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 21:00:53 2018

@author: liu431
"""

def is_simple_name(city_name):
    if len(city_name)>0:
        for character in city_name:
            character=str(character)
            if character.islower()and not character.isspace()and character.isalpha():
                continue
            else:
                return False
        return True
    else:
        return False


T=int(input("")) #number of test cases
for i in range(T):
    n=int(input("")) #number of places
    count=0
    cities_set=set()
    for i in range(n):
        x=input("")
        if x not in cities_set:
             cities_set.add(x) 
             if is_simple_name(x):
                 count+=1
       
    print(count)       
          
        