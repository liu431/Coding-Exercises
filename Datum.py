# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 18:05:14 2018

@author: LI LIU
"""
from datetime import date

days = [
        'Monday',
        'Tuesday',
        'Wednesday',
        'Thursday',
        'Friday',
        'Saturday',
        'Sunday',
]
day, month = [int(s) for s in input().split()]
date = date(2009, month, day)
print(days[date.weekday()])  