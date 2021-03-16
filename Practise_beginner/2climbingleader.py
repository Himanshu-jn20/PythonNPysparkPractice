# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 02:20:33 2020

@author: Himanshu
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 20:38:31 2020

@author: Himanshu
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbingLeaderboard(ranked, player):    # Write your code here
    ranked = list(set(ranked))
    ranked.sort()
    ranked.reverse()
    #print(ranked)
    rnk_pl=[]
    rankedl=len(ranked)
    for i in player:
        if i >= ranked[-1]:
            for j in range(rankedl):
                if i >= ranked[j]:
                    rnk_pl.append(j+1)
                    break
        else:
            rnk_pl.append(rankedl+1)

    return rnk_pl


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)
    print(result)
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()