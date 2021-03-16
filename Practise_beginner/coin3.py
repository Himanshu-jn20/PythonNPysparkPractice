# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 18:56:25 2020

@author: Himanshu
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 18:44:47 2020

@author: Himanshu
"""

# A Dynamic Programming based Python3 program to 
# find minimum of coins to make a given change V 
import sys 

# m is size of coins array (number of 
# different coins) 
def minCoins(coins, m, V): 
	
	# table[i] will be storing the minimum 
	# number of coins required for i value. 
	# So table[V] will have result 
	table = [sys.maxsize for i in range(V + 1)] 

	# Base case (If given value V is 0) 
	table[0] = 0

	# Initialize all table values as Infinite 
	#for i in range(1, V + 1): 
	#	table[i] = sys.maxsize 

	# Compute minimum coins required 
	# for all values from 1 to V 
	for i in range(1, V + 1): 		
		# Go through all coins smaller than i 
		for j in range(m): 
			if (coins[j] <= i): 
				sub_res = table[i - coins[j]] 
				if (sub_res != sys.maxsize and
					sub_res + 1 < table[i]): 
					table[i] = sub_res + 1
	print(table)
	if table[V] == sys.maxsize:
		table[V] = -1
	return(table[V])
    

# Driver Code 
if __name__ == "__main__": 

	coins = [1,2,5,10,100] 
	m = len(coins) 
	V = 5
	print(
				minCoins(coins, m, V)) 
    
    

# This code is contributed by ita_c 