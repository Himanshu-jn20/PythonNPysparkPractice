# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 21:46:19 2020

@author: Himanshu
"""
import math

s=input()

l=len(s)
k=0
subl=1
sub=[1]

if l == 1:
    print(1)
elif l== 0:
    print(0)

i=1
subm=1
while 1<=i<l:
    if s[i] in s[k:i]:
        if subm < subl:
            subm=subl
        k=k+1
        i=k+1
        subl=1
        print(i,k)
    else:
        subl=subl+1
        i=i+1
        
if subm < subl:
    print(subl)
else:
    print(subm)
        