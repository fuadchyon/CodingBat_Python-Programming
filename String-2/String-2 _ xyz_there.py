# Problem:
# Return True if the given string contains an appearance of "xyz" where the
# xyz is not directly preceeded by a period (.). So "xxyz" counts
# but "x.xyz" does not.
# Example:
# xyz_there('abcxyz') → True
# xyz_there('abc.xyz') → False
# xyz_there('xyz.abc') → True


def xyz_there(str):
    T_str = str.count('xyz')
    F_str = str.count('.xyz')
    if T_str > F_str:
        return True
    else:
        return False
