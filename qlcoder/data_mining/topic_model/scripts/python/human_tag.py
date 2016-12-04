# ~/anaconda2/bin/python
# coding:utf-8

import operator
import re
# with open('output_all_words_sorted.txt') as ifs:
#     lines = ifs.readlines()
#     data_list = map(lambda ele: ele.rstrip().split(' '), lines)
#     data_list = map(lambda ele: [ele[0].split(':')[1], ele[1].split(':')[1].split(',')], data_list)
#     print len(data_list)
#     frequency_dict = dict()
#     for words in data_list:
#         for word in words[1]:
#             if word not in frequency_dict:
#                 frequency_dict[word] = 0
#             frequency_dict[word] += 1
#
#     print len(frequency_dict)
#
#     sorted_x = sorted(frequency_dict.items(), key=operator.itemgetter(1))[::-1]
#     with open('frequency_top_words_1000.txt', 'w') as ofs:
#         for i in range(1000):
#             print sorted_x[i][0], sorted_x[i][1]
#             ofs.write(' '.join([sorted_x[i][0], str(sorted_x[i][1])]) + '\n')

word_list = []
for i in range(8000):
    with open('../8000_words/' + str(i) + '.txt') as ifs:
        lines = ifs.readlines()
        lines = list(set(map(lambda line: line.strip(), lines)))
        word_list.append(lines)

print len(word_list)
frequency_dict = dict()
for words in word_list:
    for word in words:
        if word not in frequency_dict:
            frequency_dict[word] = 0
        frequency_dict[word] += 1
print len(frequency_dict)

sorted_x = sorted(frequency_dict.items(), key=operator.itemgetter(1))[::-1]
with open('frequency_top_words.txt', 'w') as ofs:
    for i in range(2000):
        # print sorted_x[i][0], sorted_x[i][1]
        ofs.write(' '.join([sorted_x[i][0], str(sorted_x[i][1])]) + '\n')
