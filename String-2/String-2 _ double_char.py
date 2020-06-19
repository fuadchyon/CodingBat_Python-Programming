# Problem:
# Given a string, return a string where for every char in the original,
# there are two chars.
# Exercise:
# double_char('The') → 'TThhee'
# double_char('AAbb') → 'AAAAbbbb'
# double_char('Hi-There') → 'HHii--TThheerree'


def double_char(str):
    n_str = ""
    for char in str:
        n_str = n_str+char*2
    return n_str
