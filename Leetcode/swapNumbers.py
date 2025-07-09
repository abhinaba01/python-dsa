class Solution:
    def swap(self, a, b):
       
      a = a ^ b
      b = a ^ b
      a = a ^ b

      return a , b
    
sol = Solution()
print(sol.swap(-10,15))