# Problem:
# Given three ints, a b c, return True if one of b or c
# is "close" (differing from a by at most 1), while the other is "far",
# differing from both other values by 2 or more. Note: abs(num) computes
# the absolute value of a number.
# Exercise:
# close_far(1, 2, 10) → True
# close_far(1, 2, 3) → False
# close_far(4, 1, 3) → True


def close_far(a, b, c):
    if abs(a-b) == 1 and abs(b-c) == 1:
        return False
    elif abs(c-a) == 1 and abs(a-b) == 1:
        return False
    elif abs(b-c) == 1 and abs(c-a) == 1:
        return False
    elif a == b or b == c or c == a:
        return True
    elif abs(a-b) == 1 or abs(b-a) == 1:
        return True
    elif abs(b-c) == 1 or abs(c-b) == 1:
        return True
    elif abs(c-a) == 1 or abs(a-c) == 1:
        return True
    else:
        return False
