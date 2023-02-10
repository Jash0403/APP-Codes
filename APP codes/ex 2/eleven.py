def even(L):
    even_nos = [num for num in L if num % 2 == 0]
    return even_nos


list1 = [10, 21, 4, 45, 66, 93]


print("Even numbers in the list: ", even(list1))
