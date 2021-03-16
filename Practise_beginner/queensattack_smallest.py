# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 12:18:17 2020

@author: Himanshu
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the queensAttack function below.
def queensAttack(n, k, r_q, c_q, obstacles):
    x_cor=[0,0,1,-1,1,-1,1,-1]
    y_cor=[1,-1,1,-1,0,0,-1,1]
    r_q1=r_q
    c_q1=c_q
    
    ans=0
    for j in range(8):
        r_q=r_q1
        c_q=c_q1
        move=0
        counter=1
        while 0<r_q+x_cor[j]<=n and 0<c_q+y_cor[j]<=n and counter<n:
            counter=counter+1
            if [r_q+x_cor[j],c_q+y_cor[j]] not in obstacles:
                move=move+1
                r_q=r_q+x_cor[j]
                c_q=c_q+y_cor[j]
            else:
                break                
        ans=ans+move
    result=ans
    return result

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    r_qC_q = input().split()

    r_q = int(r_qC_q[0])

    c_q = int(r_qC_q[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))
    
    result = queensAttack(n, k, r_q, c_q, obstacles)
    print(result)

    #fptr.write(str(result) + '\n')

    #fptr.close()
