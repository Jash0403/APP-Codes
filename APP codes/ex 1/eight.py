for i in range(100, 401):
    if i % 10 % 2 == 0 and i % 100//10 % 2 == 0 and i % 1000//100 % 2 == 0:
        print(i, end=", ")
