#User function Template for python3

class Solution:
    def minPartition(self, N):
        
        denominations = [2000,500,200,100,50,20,10,5,2,1]
        coins = []
        
        for den in denominations:
            
            cnt = N // den
            coins.extend([den] * cnt)
            N = N % den
            
        return coins
            
            
        
        