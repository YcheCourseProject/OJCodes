# from wiki: https://en.wikipedia.org/wiki/Burrows%E2%80%93Wheeler_transform#Example

origin_str = '^BANANA|'


def bwt(s):
    table = sorted(s[i:] + s[:i] for i in range(len(s)))  # Table of rotations of string
    last_column = [row[-1:] for row in table]  # Last characters of each row
    return "".join(last_column)


def ibwt(r):
    table = [""] * len(r)  # Make empty table
    for i in range(len(r)):
        table = sorted(r[i] + table[i] for i in range(len(r)))  # Add a column of r
    s = [row for row in table if row.endswith("|")][0]  # Find the correct row (ending in "\0")
    return s


encoded_str = bwt(origin_str)
print encoded_str
decoded_str = ibwt(encoded_str)
print decoded_str

