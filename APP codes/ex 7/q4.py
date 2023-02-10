from functools import reduce


def average(nums):
    return reduce(lambda x, y: x + y, nums) / len(nums)


nums = (23, 12, 33)
print(average(nums))
