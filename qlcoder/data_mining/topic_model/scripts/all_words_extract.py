# ~/anaconda2/bin/python
# coding:utf-8

import re


def is_filtered_pattern(your_str):
    your_str = str(your_str)
    if re.match('[a-zA-Z]+', your_str):
        return True


with open('../output_all.txt') as ifs:
    lines = ifs.readlines()
    lines = map(lambda line: line.lstrip().rstrip(), lines)
    all_words = []
    for line in lines:
        all_words.extend(filter(lambda ele: len(ele) > 0, re.split(r'\s|&.*|;',line)))
    print len(all_words)
    all_words.sort()
    all_words = set(all_words)
    with open('../output_all_sorted.txt', 'w') as ofs:
        ofs.write('\n'.join(all_words))
