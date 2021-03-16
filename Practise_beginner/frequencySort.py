# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 23:05:45 2020

@author: Himanshu
"""

a=[1,2,2,3,3,3]
a1=set(a)
a3=list(a1)
a2=list(a1)
b=[]
b1=[]
print(f'a2 is {a2}' )
print(f'a3 is {a2}' )
for i in a1:
    val=a.count(i)
    b.append(val)

b1=b.copy()

b.sort()
b.reverse()
print(f'b1 is {b1}' )
print(f'b is {b}' )

for i in range(len(b)):
    print(b1[i])
    c=b.index(b1[i])
    print(f'c is - {c}')
    a2[c]=a3[i]

print(a2)

    
    
        
    