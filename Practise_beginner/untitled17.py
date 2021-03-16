# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 14:55:01 2020

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
    amt=int(input('amt -'))
    notes=0       
    
    while amt!=0 :
        currency=[1,3,4,5]
        
        near_curr=currency[-1]
        for val in currency:
            if amt < val:
                print ('val -' + str(val))
                near_curr=currency[currency.index(val) - 1]
                break
        
        print('near_curr -' + str(near_curr))
        notes=notes + (amt//near_curr)
        amt=amt%near_curr
        print('notes-' + str(notes) +', amt-' + str(amt))
        