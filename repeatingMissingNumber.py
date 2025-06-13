from typing import List

def repeatingMissingNumber(nums:List[int]):

    hashMap = {}

    sum , el = 0 , 0
                   
    for num in nums:
        sum+=num
        if num in hashMap:
            hashMap[num] += 1
            if hashMap[num] == 2:
                el = num
        else:
            hashMap[num] = 1

    
    N = len(nums)
    actual_sum = (N * (N+1))// 2
    diff = sum - actual_sum 

    return   el - diff,el

    

    

    

if __name__ == "__main__":
    N = int(input("Enter a number: "))
    arr =  []
    for i in range(1,N+1):
        arr.append(i)

    
    arr.remove(10)
    arr.append(18)

    diff = repeatingMissingNumber(arr)
    print("The number reversed is:", diff) 


    
