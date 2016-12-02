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
    else:
        if re.match('badcase.*', line_str):
            bad_case_set.add(line_str.split()[1])
            return True

        return False


with open('../8000/1.txt') as ifs:
    lines = ifs.readlines()
    lines = map(lambda ele: ele.rstrip().lstrip(), lines)
    lines = filter(lambda ele: not is_bad_pattern(ele), lines)
    for line in lines:
        print 'line:', line

for ele in bad_case_set:
    print bad_case_set
