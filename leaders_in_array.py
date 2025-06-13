from typing import List


def leadersinArray(nums:List[int]):
    l = float("-inf")
    list_leaders,i = [],len(nums) - 1
    while i > 0:
        if nums[i] > l:
            list_leaders.insert(0,nums[i])
            l = nums[i]
        i-=1
        

    print(list_leaders)
        

if __name__ == '__main__':
    arr = [-3, 4, 5, 1, -4, -5]
    leadersinArray(arr)
    
