for i in range(0, 9):
    c = i + 1
    if i > 4:
        c = 9 - i

    for j in range(0, c):

        print("* ", end="")

    print()
