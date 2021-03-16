# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 13:09:27 2020

@author: Himanshu
"""

n=int(input())
n_op=int(input())

arr=[0]*n
sum1=0
while n_op!=0:
    n_op=n_op-1
    var=list(map(int,input().split()))
    type=var[0]
    rl=var[1]
    rh=var[2]
    

    for i in range(rl,rh+1):
        if type == 0:
             if arr[i]==0:
                 arr[i]=1
             else:
                arr[i]=0
        else:
            sum1=sum1+arr[i]
    
    #print(arr)
   
print(sum1%1000000007)
            