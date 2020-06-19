# Problem:
# Given a string of even length, return the first half.
# So the string "WooHoo" yields "Woo".
# Example:
# first_half('WooHoo') → 'Woo'
# first_half('HelloThere') → 'Hello'
# first_half('abcdef') → 'abc'


def first_half(str):
    if len(str) % 2 != 0:
        return("Error")
    str_half = int(len(str)/2)
    return(str[:str_half])
