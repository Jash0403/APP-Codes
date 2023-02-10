def all_different(seq):
    return len(set(seq)) == len(seq)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(all_different(numbers))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]

print(all_different(numbers))
