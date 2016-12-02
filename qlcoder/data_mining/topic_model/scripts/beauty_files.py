# ~/anaconda2/bin/python
# coding:utf-8

import sys
import re

reload(sys)
sys.setdefaultencoding("utf8")


def is_bad_pattern(your_str):
    if len(your_str.rstrip().lstrip()) == 0:
        return True
    your_str = str(your_str)
    if re.match('.*&.;*', your_str):
        return True


with open('../8000/7984.txt') as ifs:
    lines = ifs.readlines()
    lines = map(lambda ele: ele.rstrip(), lines)
    lines = filter(lambda ele: not is_bad_pattern(ele), lines)
    for line in lines:
        print line
