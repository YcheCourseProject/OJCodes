# ~/anaconda2/bin/python
# coding:utf-8

import re

import all_words_extract as yche_util
import jieba.analyse
import jieba.posseg


def extract_link(lines):
    links = []
    for line in lines:
        if re.match(r'.*\[.*\]', line):
            links.extend(re.findall(r'\[.*\]', line))
        if re.match(r'\xe3\x80\x90.*\xe3\x80\x91', line):
            links.extend(re.findall(r'\xe3\x80\x90.*\xe3\x80\x91', line))
    return links


lines = yche_util.remove_duplicate(yche_util.get_lines_single_file('../8000/4324.txt'))
map_res = map(lambda line: jieba.posseg.cut(line), lines)
words = reduce(lambda left, right: list(left) + list(right), map_res)
# words = filter(lambda word, tag: word not in yche_util.stop_words_set and not re.match(r'[0-9]+', word), words)
for word, tag in words:
    print word, tag
