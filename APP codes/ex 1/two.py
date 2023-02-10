import random


x = -1
val = 0

while x != val:
    x = random.randint(1, 9)
    val = int(input("Enter your guess: "))
    print("Generated value: {} \n".format(x))
    if x == val:
        print("Well Guessed!")
        break
