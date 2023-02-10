def add_list(list):
    result = 0
    for i in list:
        result += i
    return result


def difference(list1, list2):
    return add_list(list2) - add_list(list1)


list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


print(difference(list1, list2))
