def prime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


num = int(input("Enter a number: "))

if prime(num) == True:
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")
