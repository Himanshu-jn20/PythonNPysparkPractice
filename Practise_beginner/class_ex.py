# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 15:47:53 2020

@author: Himanshu
"""

class Person:
    def __init__(self,name):
        self.name=name
        
    def talk(self):
        print(self.name,' can talk')
        
himanshu=Person('Jain')

himanshu.talk()