import math


def checkArmstrong(num):
    #num_digits = count_num_digits(num)
    num_digits = len(str(num))
    
    sum ,d = 0,0
    while num > 0:
        d = num % 10
        sum = sum + (d ** num_digits)
        num = num // 10
    
    return sum
    
    
    
def count_num_digits(num):
    count = int(math.log10(num) + 1)
    
    return count


if __name__ == "__main__":
    n = int(input("Enter a number: "))
    sum = checkArmstrong(n)
    if sum == n:
        print("It is a Armstrong number")
    else:
        print("It is not a Armstrong number")



   