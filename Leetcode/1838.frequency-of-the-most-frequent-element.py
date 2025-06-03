#
# @lc app=leetcode id=1838 lang=python3
#
# [1838] Frequency of the Most Frequent Element
#

# @lc code=start
from typing import List



class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        count,max_num,l,r = 0,float("-inf"),0,1
        def check(l,r,k):
           
            if  ((r-l) * nums[r] - sum(nums[l:r])) <= k:
                return (r-l+1)
            else:
                return -10000000
      
        while l < len(nums)-1 and r < len(nums):
            count = check(l,r,k)
            max_num = count if count > max_num else max_num
            
            if count > 0:    
                r+=1
            else:
                l+=1
        return max_num


if __name__ == '__main__':
    arr = [1,4,8,13]
    print(Solution.maxFrequency(Solution,arr,5))
    


        
# @lc code=end

