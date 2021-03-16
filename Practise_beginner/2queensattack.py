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
        for i in range(1,n):            
            #print ('start cor-' +str(r_q)+','+str(c_q) +'xy-' +str(x_cor[j])+','+str(y_cor[j]))
            if r_q+x_cor[j]>n or r_q+x_cor[j]<=0:
                #print('r_q out  j i' + str(j) +','+str(i))
                break
            elif c_q+y_cor[j]>n or c_q+y_cor[j]<=0:
                #print('c_q out  j i' + str(j) +','+str(i))
                break
            elif [r_q+x_cor[j],c_q+y_cor[j]] not in obstacles:
                move=move+1
                r_q=r_q+x_cor[j]
                c_q=c_q+y_cor[j]
                #print('in  j i' + str(j) +','+str(i)+ 'move-' +str(move))
                #print(r_q,c_q)
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
