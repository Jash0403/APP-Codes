# Write a Python program to convert a given list of strings into list of lists using map function.


def convert_to_list_of_lists(lst):
    return list(map(lambda x: [x], lst))


lst = ['a', 'b', 'c', 'd', 'e']
print(convert_to_list_of_lists(lst))
