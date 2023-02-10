def filter_array(array):
    return list(filter(lambda x: x >= 18, array))


print(filter_array([12, 23, 34, 45, 1, 5, 18]))
