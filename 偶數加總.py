# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 16:54:50 2021

@author: User
"""
a=int(input())
total=0
for num in range(a+1):
    if num % 2==0:
       total=total+num
print("總計偶數總和為", total)
print('20210306')