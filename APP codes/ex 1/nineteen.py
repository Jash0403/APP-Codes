def reverse_digits(n):
    sum = 0
    while n > 0:
        sum = sum * 10 + n % 10
        n = n // 10
    return sum


n = int(input("Enter a number: "))

while n != reverse_digits(n):
    n += reverse_digits(n)
    print(n)
