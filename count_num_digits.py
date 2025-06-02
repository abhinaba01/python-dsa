

import math


def countDigits(n):
    count = int(math.log10(n)+1)
    return count
        
        

if __name__ == "__main__":
    N = int(input("Enter a number: "))
    print("N:", N)
    digits = countDigits(N)
    print("Number of Digits in N:", digits)




