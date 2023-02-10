def sort_numeric_strings(nums_str):
    result = sorted(nums_str, key=lambda el: int(el))
    return result


nums_str = ['4', '12', '45', '7', '0', '100', '200', '-12', '-500']

print("\nSortint the list of strings(numbers) numerically:")
print(sort_numeric_strings(nums_str))