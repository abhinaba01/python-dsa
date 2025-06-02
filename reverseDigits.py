def rev_digits(n:int):
    x_rev,d = 0,0
    while n > 0:
        d = n % 10
        x_rev = x_rev * 10 + d
        n = n // 10
    return x_rev   

if __name__ == "__main__":
    N = int(input("Enter a number: "))
    print("N:", N)
    num= rev_digits(N)
    print("The number reversed is:", num) 

