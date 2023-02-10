def filter_vowels(lst):
    return list(filter(lambda x: x in ['a', 'e', 'i', 'o', 'u'], lst))


print(filter_vowels(['a', 'g', 'e', 'j', 'k', 'u']))
