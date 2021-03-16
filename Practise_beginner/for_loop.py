# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 01:51:26 2020

@author: Himanshu
"""

prices = [10, 20, 30]
tot_price=0
for price in prices:
    tot_price=tot_price + price
print(f'tot price is {tot_price}')

#task
f_list=[5,2,5,2,2]
for val in f_list:
    print('*' * val)
    
f_list=[5,2,5,2,2]
for val in f_list:
    star=''
    for num in range(val):
        star = '*' + star
    print(star)
