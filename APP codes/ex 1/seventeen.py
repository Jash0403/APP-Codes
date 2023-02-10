def sum_of_digits(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n = n // 10
    return sum


while True:
    try:
        n = int(input("Enter a positive integer: "))
        if n < 0:
            print("Please enter a positive integer")
            continue
        break
    except ValueError:
        print("Please enter a positive integer")
        continue

while n > 0:
    n -= sum_of_digits(n)
    if n != 0:
        print(n)
