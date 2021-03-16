# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 01:02:01 2020

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
        k=k+s[k:i].index(s[i])+1 #sliding the window
        subl=i+1-k
        #print(k,i)
        #print('subl is-',subl)
    else:
        subl=subl+1
        #print('subl b-',subl)
    #print('subm is-',subm)
    i=i+1
        
if subm < subl:
    print(subl)
else:
    print(subm)
        