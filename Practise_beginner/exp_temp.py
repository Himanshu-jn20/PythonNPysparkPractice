# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 15:53:36 2020

@author: Himanshu
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 15:13:02 2020

@author: Himanshu
"""

#!/bin/python3

import math


nd=input().split()
n=int(nd[0])
d=int(nd[1])
med=d/2
mod=d%2

med_val=math.floor(med)


exp_main=input().split()
if len(exp_main) != n:
    print('Provide 9 days expenditure')
    exit(0)

notification=0
for i in range(n-d):
    exp=exp_main[i:d+i]
    exp.sort()
    if mod != 0:
        lim=2 * int(exp[med_val])            
    else:
        lim=2 * (int(exp[med_val-1]) + int(exp[med_val]))/2
    
    if int(exp_main[d+i]) >= lim:
            notification=notification+1

print(notification)
    