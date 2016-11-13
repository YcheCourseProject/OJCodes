old = "yxacab"


def decode_game_coding(game_str):
    str_list = list()
    for i in range(0, len(game_str) / 2):
        my_ch = game_str[i * 2]
        my_ch_count = int(game_str[i * 2 + 1])
        str_list.append(my_ch * my_ch_count)
    return ''.join(str_list)


def get_encoded_bwt_str():
    with open('144957540328740.txt') as fs:
        line = fs.readline()
        line = line[0:len(line) - 1]
        # print line
    return decode_game_coding(line)


def encode_str_bwt(old_str):
    arr = []
    idx = 0
    for ele in old_str:
        arr.append([ele, idx])
        idx += 1
    print arr
    arr.sort(lambda left, right: ord(left[0]) - ord(right[0]))
    print arr
    encoded_str = ''.join(map(lambda ele: ele[0], arr))
    return encoded_str


print 'old:', old
encoded_str = encode_str_bwt(old)
print 'encoded:', encoded_str

print get_encoded_bwt_str()
with open('bwt_intermediate.txt', 'w') as ofs:
    ofs.write(get_encoded_bwt_str())


def ibwt(r):
    """Apply inverse Burrows-Wheeler transform."""
    table = [""] * len(r)  # Make empty table
    for i in range(len(r)):
        table = sorted(r[i] + table[i] for i in range(len(r)))  # Add a column of r
    s = [row for row in table if row.endswith(" ")][0]  # Find the correct row (ending in "\0")
    return s.rstrip(" ")  # Get rid of trailing null character


print encode_str_bwt('SIX.MIXED.PIXIES.SIFT.SIXTY.PIXIE.DUST.BOXES')
print ibwt(get_encoded_bwt_str())

# id = 0
# new = ""
# while True:
#     new += a[id][0];
#     id = a[id][1];
