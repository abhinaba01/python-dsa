from sys import stdin
import sys

def cutRod(price, n):

    
    dp = [0] * (n+1)
    for i in range(n + 1):
        for j in range(len(price)):
            if i - j - 1 >= 0:
                dp[i] = max(dp[i-j-1] + price[j] , dp[i] )


    return dp[n]

    

# Taking input using fast I/O.
def takeInput():
    n = int(input())

    price = list(map(int, input().strip().split(" ")))

    return price, n
