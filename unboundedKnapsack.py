from typing import List

def unboundedKnapsack(n: int, w: int, profit: List[int], weight: List[int]) -> int:
    
    dp = [0] * (w+1)


    for i in range(w+1):
        for j in range(n):
            if i - weight[j] >= 0:
                dp[i] = max(dp[i-weight[j]] + profit[j],dp[i])

    return dp[w]