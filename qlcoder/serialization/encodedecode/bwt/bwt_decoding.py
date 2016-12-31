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


def ibwt(r):
    firstCol = "".join(sorted(r))
    count = [0] * 256
    byteStart = [-1] * 256
    output = [""] * len(r)
    shortcut = [None] * len(r)
    # Generates shortcut lists
    for i in range(len(r)):
        shortcutIndex = ord(r[i])
        shortcut[i] = count[shortcutIndex]
        count[shortcutIndex] += 1
        shortcutIndex = ord(firstCol[i])
        if byteStart[shortcutIndex] == -1:
            byteStart[shortcutIndex] = i

    localIndex = (r.index("|"))
    for i in range(len(r)):
        # takes the next index indicated by the transformation vector
        nextByte = r[localIndex]
        output[len(r) - i - 1] = nextByte
        shortcutIndex = ord(nextByte)
        # assigns localIndex to the next index in the transformation vector
        localIndex = byteStart[shortcutIndex] + shortcut[localIndex]
    return "".join(output).rstrip("|")


with open('output_bwt.txt', 'w') as ofs:
    answer = ibwt(get_encoded_bwt_str())
    ofs.write(answer)
