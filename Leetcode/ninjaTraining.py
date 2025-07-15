#User function Template for python3

class Solution:
    def maximumPoints(self, arr):
        
        
        n = len(arr)
        dp = [[-1 for _ in range(n+1)] for _ in range(3)]
        
        
        def dfs(i,k):
            
            if dp[k][i] != -1:
                    return dp[k][i]
                    
            
            if i > n - 1:
                return 0
                
            
            if k == 0:
                
            
                dp[0][i] = arr[i][0] + max(dfs(i+1,1), dfs(i+1,2))
                return dp[0][i]
    
            if k == 1:
                
                dp[1][i] =  arr[i][1] + max(dfs(i+1,0),dfs(i+1,2))
                return dp[1][i]
                
            if k == 2:
                
                dp[2][i] = arr[i][2] + max(dfs(i+1,0) ,dfs(i+1,1))
                return dp[2][i]
                
       
                
                
        return max(dfs(0,0),dfs(0,1),dfs(0,2))
                
            
                