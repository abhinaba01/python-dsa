


def countGoodSubsequence(name):
    MOD = 10**9 + 7
    freq = {}
    
    for ch in name:
        freq[ch] = freq.get(ch,0) + 1
    
    maxFreq = max(freq.values())
    
    def countSubsequences(k):
        cnt = 0
        for key,value in freq.items():
            if value >= k:
                cnt += 1
        return (2 ** cnt - 1) % MOD
        

    count = 0
    for i in range(1,maxFreq+1):
        count = (count + countSubsequences(i)) % MOD
    
    return count
    


if __name__ == "__main__":
   
    ans = countGoodSubsequence("abca")
    print("Number of Good Subsequences", ans)


