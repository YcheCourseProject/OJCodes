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


def extract_link(lines):
    links = []
    for line in lines:
        if re.match(r'.*\[.*\]', line):
            links.extend(re.findall(r'\[.*\]', line))
        if re.match(r'\xe3\x80\x90.*\xe3\x80\x91', line):
            links.extend(re.findall(r'\xe3\x80\x90.*\xe3\x80\x91', line))
    return links


lines = remove_duplicate(get_lines_single_file('../8000/2.txt'))
for line in lines:
    print  line
links = extract_link(lines)
if len(links) > 0:
    print 'links:' + ''.join(links)
