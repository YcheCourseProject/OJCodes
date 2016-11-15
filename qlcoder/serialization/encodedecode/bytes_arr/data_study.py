import struct


def read_file():
    with open('task_142_test1 .txt') as ifs:
        lines = ifs.readlines()
        lines = ' '.join(lines)

        lst = map(lambda ele: int(ele.rstrip()), lines.split(' '))
        my_min = min(lst)
        print 'min:', my_min, map(ord, struct.pack('i', my_min))
        my_max = max(lst)
        print 'max:', my_max, map(ord, struct.pack('i', my_max))
    return lst


def test_bs():
    my_lst = read_file()
    filtered_lst = filter(lambda ele: is_int16(ele), my_lst)
    print len(filtered_lst)
    print len(my_lst)
    bs = BitSet(len(my_lst))
    print len(bs)
    print bs.size()


class BitSet:
    def __init__(self, size=0):
        self._size = size
        self._v = bytearray((size + 7) / 8)

    def __len__(self):
        return self._size

    def __getitem__(self, pos):
        return 1 & (self._v[pos / 8] >> pos % 8)

    def __setitem__(self, pos, val):
        if val == 0:
            self._v[pos / 8] &= ~(1 << pos % 8)
        else:
            self._v[pos / 8] |= (1 << pos % 8)

    def to_bytearray(self):
        return self._v

    def from_bytearray(self, ba):
        self._size = len(ba) * 8
        self._v = ba

    def size(self):
        return len(self.to_bytearray())


def is_int16(number):
    if -32767 <= -number <= 32768:
        return True


def write_to_buffer(nums):
    buf = bytearray()
    header_bytes = struct.pack('i', len(nums))
    buf.extend(header_bytes)

    my_bs = BitSet(len(nums))
    my_bytes_lst = []
    for i in range(len(nums)):
        if is_int16(nums[i]):
            my_bs[i] = 1
            for ele in struct.pack('h', nums[i]):
                my_bytes_lst.append(ele)
        else:
            my_bs[i] = 0
            for ele in struct.pack('i', nums[i]):
                my_bytes_lst.append(ele)
    buf.extend(my_bs.to_bytearray())
    buf.extend(my_bytes_lst)
    return buf


def read_from_buffer(buf):
    nums = []
    size = struct.unpack('i', buf[0:4])[0]
    my_bs = BitSet(size)
    my_bs.from_bytearray(buf[4:4 + (size + 7) / 8])

    start_offset = 4 + (size + 7) / 8
    for i in range(size):
        if my_bs[i] == 1:
            nums.append(struct.unpack('h', buf[start_offset:start_offset + 2])[0])
            start_offset += 2
        else:
            nums.append(struct.unpack('i', buf[start_offset:start_offset + 4])[0])
            start_offset += 4
    return nums


my_lst = read_file()
my_buf = write_to_buffer(my_lst)
my_lst2 = read_from_buffer(my_buf)
print len(my_lst)
print len(my_lst2)
for i in range(0, len(my_lst)):
    if my_lst[i] != my_lst2[i]:
        print 'error'
        # else:
        #     print 'ok'
