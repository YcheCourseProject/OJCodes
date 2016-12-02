# ~/anaconda2/bin/python
# coding:utf-8

import sys
import operator

reload(sys)
sys.setdefaultencoding("utf8")

with open('output_readable.txt') as ifs:
    lines = ifs.readlines()
    data_list = map(lambda ele: ele.rstrip().split(' '), lines)
    data_list = map(lambda ele: [ele[0].split(':')[1], ele[1].split(':')[1].split(',')], data_list)
    print len(data_list)
    frequency_dict = dict()
    for words in data_list:
        for word in words[1]:
            if word not in frequency_dict:
                frequency_dict[word] = 0
            frequency_dict[word] += 1

    print len(frequency_dict)

    sorted_x = sorted(frequency_dict.items(), key=operator.itemgetter(1))[::-1]
    with open('frequency_top_1000.txt', 'w') as ofs:
        for i in range(1000):
            print sorted_x[i][0], sorted_x[i][1]
            ofs.write(' '.join([sorted_x[i][0], str(sorted_x[i][1])]) + '\n')
