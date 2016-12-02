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
    count = 0
    min_val = 99999
    max_val = -1
    for i in range(8000):
        lines = get_lines_single_file('../8000/' + str(i) + '.txt')
        if len(lines) < 2:
            min_val = min_val if len(lines[0]) > min_val else len(lines[0])
            max_val = max_val if len(lines[0]) < max_val else len(lines[0])
            if len(lines[0]) > 200:
                print i, lines[0]
            count += 1
    print count
    print min_val, max_val


get_sorted_lines()
