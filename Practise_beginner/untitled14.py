# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 21:29:56 2020

@author: Himanshu
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 15:13:02 2020

@author: Himanshu
"""

#!/bin/python3

#!/bin/python3

import math


nd=list(map(int, input().rstrip().split()))
n,d = nd
med=d/2
mod=d%2

med_val=math.floor(med)


exp_main=list(map(int, input().rstrip().split()))

notification=0
for i in range(n-d):
    exp=exp_main[i:d+i]
    exp.sort()
    if mod != 0:
        lim=2 * exp[med_val]            
    else:
        lim=2 * (exp[med_val-1] + exp[med_val])/2
    
    if int(exp_main[d+i]) >= lim:
            notification=notification+1

print(notification)
    

    