# ~/anaconda2/bin/python
# coding:utf-8

import re

all_eng_count = 0

noise_words_first = ['可能与主题无关的词', 'badcase', '噪音词', ]
noise_words_second = ['IT', '健康', '体育', '旅游', '教育', '文化', '军事', '财经']
noise_words = []
for first in noise_words_first:
    for second in noise_words_second:
        noise_words.append(first + second)
stop_words = [r'\xe3\x80\x80', r'&nbsp;', r'&nbsp', r'&gt;', r'&gt', r'\x00', r'\s']


def remove_regex(regex_str_list, lines):
    ret_lines = []
    for line in lines:
        ret_lines.extend(re.sub('|'.join(regex_str_list), '', line).split())
    return ret_lines


def get_lines_single_file(file_name):
    with open(file_name) as ifs:
        lines = ifs.readlines()
        lines = remove_regex(stop_words, lines)
        lines = remove_regex(noise_words, lines)

        eng_words = []
        for line in lines:
            if re.match('.*[a-zA-Z]+.*', line):
                for ele in re.findall('[a-zA-Z]+', line):
                    eng_words.append(ele)

        all_words_count = len(''.join(lines))
        eng_words_count = len(''.join(eng_words))
        global all_eng_count
        if float(eng_words_count) / all_words_count > 0.3:
            all_eng_count += 1
        return lines


def remove_duplicate(lines):
    my_set = set()
    ret_lines = []
    for line in lines:
        if line not in my_set:
            my_set.add(line)
            ret_lines.append(line)
    return ret_lines


def get_sorted_lines():
    for i in range(8000):
        lines = remove_duplicate(get_lines_single_file('../8000/' + str(i) + '.txt'))
        with open('../8000_copy/' + str(i) + '.txt', 'w') as ofs:
            ofs.write('\n'.join(lines))


get_sorted_lines()
print all_eng_count
