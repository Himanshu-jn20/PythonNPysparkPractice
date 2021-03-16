#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the queensAttack function below.
def queensAttack(n, k, r_q, c_q, obstacles):
    move=[0 for i in range(8)]
    #table = [0 for i in range(5 + 1)]
    block = [0 for i in range(8)]
    
    
#for j in range(8)
    for i in range(1,n):
        
        if c_q+i<=n and [r_q,c_q+i] not in obstacles and block[0]==0:
            move[0]=move[0]+1
        else:
            block[0]=1

        if c_q-i>0 and [r_q,c_q-i] not in obstacles and block[1]==0:
            move[1]=move[1]+1
        else:
            block[1]=1

        if r_q+i<=n and c_q+i<=n and [r_q+i,c_q+i] not in obstacles and block[2]==0:
            move[2]=move[2]+1
        else:
            block[2]=1

        if r_q-i>0 and c_q-i>0 and [r_q-i,c_q-i] not in obstacles and block[3]==0:
            move[3]=move[3]+1
        else:
            block[3]=1

        if r_q+i<=n and [r_q+i,c_q] not in obstacles and block[4]==0:
            move[4]=move[4]+1
        else:
            block[4]=1

        if r_q-i>0 and [r_q-i,c_q] not in obstacles and block[5]==0:
            move[5]=move[5]+1
        else:
            block[5]=1

        if r_q+i<=n and  c_q-i>0 and [r_q+i,c_q-i] not in obstacles and block[6]==0:
            move[6]=move[6]+1
        else:
            block[6]=1

        if r_q-i>0 and c_q+i<=n and [r_q-i,c_q+i] not in obstacles and block[7]==0:
            move[7]=move[7]+1
        else:
            block[7]=1
            
   
    result=sum(move)
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
