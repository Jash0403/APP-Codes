def absent_digits(n):
    all_nums = set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    n = set([int(i) for i in n])
    n = n.symmetric_difference(all_nums)
    n = sorted(n)
    return n


n = ([])
while True:
    try:
        num = input("Enter a phone number: ")
        if len(num) != 10:
            print("Please enter a 10 digit number")
            continue
        break
    except ValueError:
        print("Please enter a 10 digit number")
        continue

for i in num:
    n.append(int(i))


print(absent_digits(n))
