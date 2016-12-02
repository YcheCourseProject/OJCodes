# ~/anaconda2/bin/python
# coding:utf-8

import sys
import re

reload(sys)
sys.setdefaultencoding("utf8")

bad_case_set = set()
irrelevant_set = set()
noise_set = set()


def is_bad_pattern(line_str):
    line_str = re.sub('&.*;', '', line_str)
    line_str = line_str.rstrip().lstrip()
    if len(line_str) == 0:
        return True
        # else:
        # if re.match('badcase.*', line_str):
        #     bad_case_set.add(line_str.split()[1])
        # return True

        # return False


def extract_link(line):
    if re.match(r'.*\[.*\]', line):
        print 'match'
        links = re.findall(r'\[.*\]', line)
        return links
    else:
        return None


with open('../8000/5.txt') as ifs:
    lines = ifs.readlines()
    new_lines = []
    for line in lines:
        new_lines.extend(re.sub(r'\xe3\x80\x80|&nbsp;|&nbsp|&gt;|&gt|\x00', '', line).split())

    new_lines = map(lambda ele: ele.rstrip().lstrip(), new_lines)
    new_lines = filter(lambda ele: not is_bad_pattern(ele), new_lines)
    new_lines = map(lambda ele: ele.lstrip().rstrip(), new_lines)

    for line in new_lines:
        print 'line:', line
        links = extract_link(line)
        if not links is None:
            print links
    print new_lines

for ele in bad_case_set:
    print bad_case_set
