# ~/anaconda2/bin/python
# coding:utf-8

import re


def get_lines_single_file(file_name):
    with open(file_name) as ifs:
        lines = ifs.readlines()
        new_lines = []
        for line in lines:
            new_lines.extend(re.sub(r'\xe3\x80\x80|&nbsp;|&nbsp|&gt;|&gt|\x00', '\n', line).split())

        ret_lines = []

        is_bad = False
        for i in range(len(new_lines)):
            line = new_lines[i]
            if is_bad:
                is_bad = False
                continue
            if re.match('.*可能与主题无关的词.*', line) or re.match('.*badcase.*', line) or re.match('.*噪音词.*', line):
                is_bad = True
                continue
            ret_lines.append(line)

        return ret_lines


def remove_duplicate(lines):
    my_set = set()
    ret_lines = []
    for line in lines:
        my_set.add(line)
        if line not in ret_lines:
            ret_lines.append(line)
    return ret_lines


def get_sorted_lines():
    for i in range(8000):
        lines = remove_duplicate(get_lines_single_file('../8000/' + str(i) + '.txt'))
        with open('../8000_copy/' + str(i) + '.txt', 'w') as ofs:
            ofs.write('\n'.join(lines))


get_sorted_lines()
