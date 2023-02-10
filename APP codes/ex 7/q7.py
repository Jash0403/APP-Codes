def convert(list):
    for i in list:
        if i.isupper():
            list.remove(i)
            list.append(i.lower())
        elif i.islower():
            list.remove(i)
            list.append(i.upper())
    return list


def eliminate_duplicates(list):
    converted_list = convert(list)
    return set(converted_list)


list = ['a', 'b', 'c', 'd', 'e', 'A', 'B',
        'C', 'D', 'E', 'a', 'b', 'c', 'd', 'e']


print(eliminate_duplicates(convert(list)))
