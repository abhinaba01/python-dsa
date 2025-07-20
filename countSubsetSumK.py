#User function Template for python3
class Solution:
    def perfectSum(self, arr, k):
        n = len(arr)
        mod = 10**9 + 7
        dp = [[0 for _ in range(k+1)] for _ in range(n)]
        
        if arr[0] == 0:
            dp[0][0] = 2  # Empty set and {0}
        else:
            dp[0][0] = 1  # Only empty set
        
        if arr[0] != 0 and arr[0] <= k:
            dp[0][arr[0]] = 1

        for i in range(1, n):
            for target in range(k+1):
                not_take = dp[i-1][target]
                take = 0
                if arr[i] <= target:
                    take = dp[i-1][target - arr[i]]
                dp[i][target] = (take + not_take) % mod

        return dp[n-1][k]


		            
		            
		        
		