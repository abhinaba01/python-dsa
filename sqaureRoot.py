def squareRoot(num:int):
    l = 1
    r = num

    if num == 0:
        return 0

    while l <= r:
        m = (l + r) // 2
        if m * m == num:
            return m
        elif m * m < num and (m + 1) * (m + 1) > num:
            return m
        elif m * m > num:
            r = m - 1
        elif m * m < num:
            l = m + 1

if __name__ == "__main__":
    N = int(input("Enter a number: "))
    print("N:", N)
    ans = squareRoot(N)
    print("Square Root of N:", ans)


