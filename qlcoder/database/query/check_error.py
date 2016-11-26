# ~/anaconda2/bin/python
# coding:utf-8

import re

if __name__ == '__main__':
    with open('/home/cheyulin/GitRepos/OJCodes/qlcoder/database/query/tuple_query/build/tmp.txt') as ifs:
        lines = ifs.readlines()
        to_used = lines[15: 15 + 13262]
        to_used = map(lambda ele: ele.lstrip().rstrip(), to_used)
        my_set = set()
        my_list = [-1]
        for ele in to_used:
            # print ele
            if not ('拉链' in ele or '其他' in ele):
                print 'bad'
                break
            tmp = ele.split(', ')
            sale_num = int(tmp[2])
            created_at = long(tmp[7])
            dsr = float(tmp[8])
            id = long(tmp[0][1:])
            my_set.add(id)
            my_list.append(id)
            print long(tmp[0][1:])
            if not (8468 <= sale_num <= 20576 and 1400703171 <= created_at <= 1442106921 and 3.7 <= dsr <= 4.6):
                print 'bad'
                break

        print '\n'
        print 'len', len(to_used), len(my_set)
        print 'first:', to_used[0]
        print 'query string:', lines[14]

        for i in range(1, len(to_used)):
            if my_list[i]==my_list[i-1]:
                print my_list[i], i
