# Problem:
# Given a string, return a "rotated left 2" version where the first 2 chars
# are moved to the end. The string length will be at least 2.
# Example:
# left2('Hello') → 'lloHe'
# left2('java') → 'vaja'
# left2('Hi') → 'Hi'


def left2(str):
    sub_str = str[2:]
    sub_str1 = str[0: 2]
    return sub_str+sub_str1
