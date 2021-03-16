# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 01:38:36 2020

@author: Himanshu
"""

txt = "hello, my name is Peter, I am 26 years old"

x = txt.split(", ")[1]
print(x)

name = 'Mosh'
message = f'Hi, my name is {name}'
print(message.upper())
print(message)

exp_main=['2', '3', '4', '2', '3', '6', '8', '4', '5']
print(exp_main)
exp_main.sort()
#ranked = list(map(int, input().rstrip().split())) # Very important
#print(ranked)

ranked = list(set(exp_main))
ranked.sort()
ranked.reverse()
print(ranked)
#ranked1=[]
ranked.append(6)
print(ranked)
#exp_main=list(map(int, input().rstrip().split()))
print('\n'.join(map(str,ranked)))
 fptr.write('\n'.join(map(str, result)))
table = [0 for i in range(5 + 1)]
print(2%5)
print(2/5)

exp=[2,3,4,5]
exp.pop(0)
print(exp)