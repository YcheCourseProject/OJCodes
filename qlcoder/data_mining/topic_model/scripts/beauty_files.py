# ~/anaconda2/bin/python
# coding:utf-8

import re

bad_case_set = set()
irrelevant_set = set()
noise_set = set()


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


def extract_link(lines):
    links = []
    for line in lines:
        if re.match(r'.*\[.*\]', line):
            links.extend(re.findall(r'\[.*\]', line))
        if re.match(r'\xe3\x80\x90.*\xe3\x80\x91', line):
            links.extend(re.findall(r'\xe3\x80\x90.*\xe3\x80\x91', line))
    return links


with open('../8000/0.txt') as ifs:
    lines = ifs.readlines()
    new_lines = []
    for line in lines:
        new_lines.extend(re.sub(r'\xe3\x80\x80|&nbsp;|&nbsp|&gt;|&gt|\x00', '', line).split())

    new_lines = map(lambda ele: ele.rstrip().lstrip(), new_lines)
    new_lines = filter(lambda ele: not is_bad_pattern(ele), new_lines)
    new_lines = map(lambda ele: ele.lstrip().rstrip(), new_lines)

    for line in new_lines:
        print 'line:', line

    links = extract_link(new_lines)
    if len(links) > 0:
        print ''.join(links)
