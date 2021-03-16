# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 01:16:20 2020

@author: Himanshu
"""

has_good_credit= False
price=1000000

if has_good_credit:
    down_payment= price * (10/100)
else:
    down_payment= price * (20/100)
    
print(f'Down payment is {down_payment}')