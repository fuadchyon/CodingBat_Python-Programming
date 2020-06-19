# Problem:
# Given an array length 1 or more of ints, return the difference between the
# largest and smallest values in the array. Note: the built-in min(v1, v2) and
# max(v1, v2) functions return the smaller or larger of two values.
# Exercise:
# big_diff([10, 3, 5, 6]) → 7
# big_diff([7, 2, 10, 9]) → 8
# big_diff([2, 10, 7, 2]) → 8

def big_diff(nums):
    if len(nums) >= 1:
        return max(nums) - min(nums)
