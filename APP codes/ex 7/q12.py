from functools import reduce


def sum_of_numbers(lst):
    return reduce(lambda x, y: x + y, lst)


def max_element(lst):
    return reduce(lambda x, y: x if x > y else y, lst)


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


print(sum_of_numbers(lst))
print(max_element(lst))
