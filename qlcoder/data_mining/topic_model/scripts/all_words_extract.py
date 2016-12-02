# ~/anaconda2/bin/python
# coding:utf-8

import re


def is_bad_pattern(line_str):
    line_str = re.sub('&.*;', '', line_str)
    line_str = line_str.rstrip().lstrip()
    if len(line_str) == 0:
        return True


def get_lines_single_file(file_name):
    with open(file_name) as ifs:
        lines = ifs.readlines()
        new_lines = []
        for line in lines:
            new_lines.extend(re.sub(r'\xe3\x80\x80|&nbsp;|&nbsp|&gt;|&gt|\x00', '\n', line).split())

        new_lines = map(lambda ele: ele.rstrip().lstrip(), new_lines)
        new_lines = filter(lambda ele: not is_bad_pattern(ele), new_lines)
        new_lines = map(lambda ele: ele.lstrip().rstrip(), new_lines)
        return new_lines


def get_sorted_lines():
    for i in range(8000):
        lines = get_lines_single_file('../8000/' + str(i) + '.txt')
        with open('../8000_copy/' + str(i) + '.txt', 'w') as ofs:
            ofs.write('\n'.join(lines))


get_sorted_lines()
