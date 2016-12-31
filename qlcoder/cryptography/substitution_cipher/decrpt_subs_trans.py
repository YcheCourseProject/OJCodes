def get_cipher_text():
    with open('subs_cipher_text.txt') as ifs:
        return ifs.readline().strip()


def transform_ch(ch, shift_num):
    if ch == ',' or ch == ' ' or ch == '.':
        return ch
    else:
        num = ord(ch) - shift_num
        if 65 <= ord(ch) <= 90:
            if num < 65:
                num += 26
        else:
            if num < 97:
                num += 26
        return chr(num)


def substitution(i, cipher_info):
    return ''.join(map(lambda my_ch: transform_ch(my_ch, i), cipher_info))


def crack_transposition(cipher, msg_col_dim):
    msg_ch_arr = ['-'] * len(cipher)
    msg_row_dim = (len(cipher) + (msg_col_dim - 1)) / msg_col_dim

    idx_step = msg_row_dim - 1
    start_change_idx = (len(cipher) % msg_col_dim + 1) * msg_row_dim - 1

    for idx in xrange(0, len(cipher)):
        final_index = idx
        if final_index >= start_change_idx:
            final_index += (final_index - start_change_idx + idx_step) / idx_step
        msg_row_idx = final_index % msg_row_dim
        msg_col_idx = final_index / msg_row_dim
        msg_idx = msg_row_idx * msg_col_dim + msg_col_idx
        msg_ch_arr[msg_idx] = cipher[idx]

    return ''.join(msg_ch_arr)


if __name__ == '__main__':
    cipher_txt = get_cipher_text()
    my_list = []
    new_str = substitution(6, cipher_txt)
    for another_i in range(2, 1276):
        res = crack_transposition(new_str, another_i)
        if len(res) != 0 and not res.__contains__('   '):
            print another_i
            print res
