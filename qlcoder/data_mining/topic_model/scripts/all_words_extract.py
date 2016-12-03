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
        ret_noise = set()
        for i in range(len(new_lines)):
            line = new_lines[i]
            if re.match('.*可能与主题无关的词.*', line):
                ret_noise.add(new_lines[i + 1])
            elif re.match('.*badcase.*', line):
                ret_noise.add(new_lines[i + 1])
            elif re.match('.*噪音词.*', line):
                ret_noise.add(new_lines[i + 1])

        if len(ret_noise) > 0:
            print file_name + ','.join(ret_noise)
        return new_lines


def get_sorted_lines():
    for i in range(8000):
        lines = get_lines_single_file('../8000/' + str(i) + '.txt')
        with open('../8000_copy/' + str(i) + '.txt', 'w') as ofs:
            ofs.write('\n'.join(lines))


get_sorted_lines()
