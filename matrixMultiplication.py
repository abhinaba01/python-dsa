class Solution:
    def matrixMultiplication(self, arr):
        
        n = len(arr)
        
        dp = [[-1 for i in range(n)] for _ in range(n) ]
        # code here
        
        def dfs(i,j):
            if i == j:
                return 0
                
            if dp[i][j] != -1:
                return dp[i][j]
                
            minMul = float("inf")
            for k in range(i,j):
                cost = dfs(i,k)  + dfs(k+1,j) + (arr[i-1] * arr[k] * arr[j])
                
                minMul = min(minMul,cost)
            dp[i][j] = minMul
            return minMul
            
        return dfs(1,n-1)
            
        