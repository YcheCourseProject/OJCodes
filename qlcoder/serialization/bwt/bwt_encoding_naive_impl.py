# from wiki: https://en.wikipedia.org/wiki/Burrows%E2%80%93Wheeler_transform#Example

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


def game_encoding(s):
    ch_list = list()
    former_ch = None
    count = -1
    for ele in s:
        if ele != former_ch:
            ch_list.append(ele)
            former_ch = ele
            count = 1
            ch_list.append(str(count))
        else:
            count += 1
            ch_list[len(ch_list) - 1] = str(count)
            if count == 9:
                former_ch = None
    return ''.join(ch_list)


def decode_game_coding(game_str):
    str_list = list()
    for i in range(0, len(game_str) / 2):
        my_ch = game_str[i * 2]
        my_ch_count = int(game_str[i * 2 + 1])
        str_list.append(my_ch * my_ch_count)
    return ''.join(str_list)


def test_bwt_ibwt():
    origin_str = '^BANANA|'
    encoded_str = bwt(origin_str)
    print encoded_str
    decoded_str = ibwt(encoded_str)
    print decoded_str


def test_bwt_game():
    print bwt('^BABABABANANABABABABABANANABABABABABANANABANANANAAHH|')
    print game_encoding(bwt('^BABABABANANABABABABABANANABABABABABANANABANANANAAHH|'))
    print decode_game_coding(game_encoding(bwt('^BABABABANANABABABABABANANABABABABABANANABANANANAAHH|')))
    print ibwt(decode_game_coding(game_encoding(bwt('^BABABABANANABABABABABANANABABABABABANANABANANANAAHH|'))))


if __name__ == '__main__':
    test_bwt_ibwt()
    test_bwt_game()
