def nRoot(num:int,N:int):
    l = 1
    r = num

    if num == 0:
        return 0

    while l <= r:
        m = (l + r) // 2
        if productN(m,N) == num:
            return m
        elif productN(m,N) < num and productN(m+1,N) > num:
            return m
        elif productN(m,N)> num:
            r = m - 1
        elif productN(m,N)< num:
            l = m + 1

def productN(num,n):
    prod = 1

    for i in range(n):
        prod = prod * num
    return prod    



if __name__ == "__main__":
    num= int(input("Enter a number: "))
    N = int(input("Enter N: "))
    ans = nRoot(num,N)
    print("Square Root of N:", ans)


