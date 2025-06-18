def countingBits(num):
    
    count = 0
    
    while num > 0:
        num &= (num-1)
        count +=  1
        

    return count 
    



if __name__ == "__main__":
    num = int(input())
    
    sum = 0
    for i in range(num):
        sum+=countingBits(i+1)

    print(sum)
  


