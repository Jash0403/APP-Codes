def count_char(text):
    result = {}
    for char in text:
        if char == ' ':
            pass
        elif char not in result:
            result[char] = 1
        else:
            result[char] += 1
    return result


text = input("Enter a string: ")
print(count_char(text))
