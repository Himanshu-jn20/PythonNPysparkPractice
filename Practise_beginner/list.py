# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 11:38:22 2020

@author: Himanshu
"""

numbers=[2,4,5,120,3,122]
print(len(numbers))
num2=numbers
print(num2)

lnum=numbers[0]
for num in numbers:
    if lnum < num :       
        lnum=num

print(lnum)


