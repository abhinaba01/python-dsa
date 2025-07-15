from os import *
from sys import *
from collections import *
from math import *

def subsetSumToK(n, k, arr):
        
        dp = {}

        def dfs(i,currentSum):

            if currentSum == 0:
                dp[(i,currentSum)] = True
                return True

            if i == n or currentSum < 0:
                return False

            if (i,currentSum) in dp:
                return dp[(i,currentSum)]

            

            dp[(i,currentSum)] = dfs(i+1,currentSum-arr[i]) or dfs(i+1,currentSum)
            return dp[(i,currentSum)]

        return dfs(0,k)
    
    
    

