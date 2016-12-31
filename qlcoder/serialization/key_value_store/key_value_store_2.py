import os
import random

FILENAME = 'key_value_tmp.txt'

mp = []


def write_file(offset, my_bytes):
    with open(FILENAME, 'r+') as ofs:
        ofs.seek(offset)
        ofs.write(my_bytes)
    return


def read_file(offset, my_length):
    if not os.path.exists(FILENAME):
        os.mknod(FILENAME)
        os.ftruncate(os.open(FILENAME, os.O_RDWR), 102400)
    with open(FILENAME, 'r') as ifs:
        ifs.seek(offset)
        return map(ord, ifs.read(my_length))


# user_code
def get(key):
    key = int(key, 16)
    return mp[key]


def put(key):
    key = int(key, 16)
    mp[key] += 1
    if mp[key] != 5 and mp[key] != 6 and mp[key] != 7:
        write_file(key, chr(mp[key]))


def init():
    global mp
    mp = read_file(0, 102400)
