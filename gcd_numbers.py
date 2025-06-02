

def gcd_numbers(n1,n2):
    if n1>0 and n2>0:
        if n1 > n2:
            return gcd_numbers(n2,n1%n2)
        else:
            return gcd_numbers(n1,n2%n1)

    elif n1 == 0:
        return n2
    elif n2 == 0:
        return n1    
   

    
if __name__ == "__main__":
    num1 = int(input("Enter two numbers: "))
    num2 = int(input("Enter two numbers: "))

    gcd = gcd_numbers(num1,num2)
    print(f"The GCD of {num1} and {num2} is: {gcd}")