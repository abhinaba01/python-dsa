
def rev_digits(n:int):
    x_rev,d = 0,0
    while n > 0:
        d = n % 10
        x_rev = x_rev * 10 + d
        n = n // 10
    return x_rev   

def checkPalindrome(num:int):
    rev_num = rev_digits(num)
    if num == rev_num:
        return f"{num} is a palindrome"
    else:
        return f"{num} is not a palindrome"


if __name__ == "__main__":
    N = int(input("Enter a number: "))
    print("N:", N)
    isPalindome = checkPalindrome(N)
    print(isPalindome) 






