# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
class Solution:
    def divisors(self, n):

        arr = []
    
        i = 2
        while n > 1:
            if n % i == 0:
                arr.append(i)
                n = n / i
            else:
                i += 1
                
        return arr
           


sol = Solution()
print(sol.divisors(360))