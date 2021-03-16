# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 17:25:09 2020

@author: Himanshu
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 00:36:00 2020

@author: Himanshu
"""

cnt=int(input('cnt -'))
while cnt!=0:
    cnt=cnt - 1
    amt=int(input())
    notes=0       
    
    while amt!=0 :
        currency=[1,2,5,10,50,100]
        
        near_curr=100
        for i in range(1,len(currency)):
            if amt < currency[i]:
                #print ('val -' + str(val))
                near_curr=currency[i - 1]
                break
        
        #print('near_curr -' + str(near_curr))
        notes=notes + (amt//near_curr)
        amt=amt%near_curr
    print('notes-' + str(notes) +', amt-' + str(amt))
        