# ~/anaconda2/bin/python
# coding:utf-8

import re
import jieba.analyse
import os

stop_words_set = set()
stop_file_name = '../../cn_stop_words.txt'

noise_words_first = ['可能与主题无关的词', 'badcase', '噪音词', ]
noise_words_second = ['IT', '健康', '体育', '旅游', '教育', '文化', '军事', '财经']
map_res = map(lambda first: [first + second for second in noise_words_second], noise_words_first)
noise_words = reduce(lambda left, right: left + right, map_res)
blank_symbols = [r'\xe3\x80\x80', r'&nbsp;', r'&nbsp', r'&gt;', r'&gt', r'\x00', r'\s']

all_eng_count = 0


def init_stop_words_set(file_name):
    global stop_words_set
    with open(file_name, 'r') as ifs:
        lines = ifs.readlines()
        stop_words_set = set(map(lambda line: line.strip(), lines))
    stop_words_set = map(lambda word: unicode(word, 'utf-8'), stop_words_set)


def remove_regex(regex_str_list, lines):
    ret_lines = []
    for line in lines:
        ret_lines.extend(re.sub('|'.join(regex_str_list), '', line).split())
    return ret_lines


def extract_eng_words(lines):
    eng_words = []
    for line in lines:
        if re.match('.*[a-zA-Z]+.*', line):
            for ele in re.findall('[a-zA-Z]+', line):
                eng_words.append(ele)
    return eng_words


def get_lines_single_file(file_name):
    with open(file_name) as ifs:
        lines = ifs.readlines()
        lines = remove_regex(blank_symbols, lines)
        lines = remove_regex(noise_words, lines)

        eng_words = extract_eng_words(lines)
        all_words_count = len(''.join(lines))
        eng_words_count = len(''.join(eng_words))
        global all_eng_count
        if float(eng_words_count) / all_words_count > 0.3:
            print 'cat' + ' ' + file_name
            all_eng_count += 1
        return lines


def remove_duplicate(lines):
    my_set = set()
    ret_lines = []
    for line in lines:
        if line not in my_set:
            my_set.add(line)
            ret_lines.append(line)
    return ret_lines


def get_words_single_file(filename):
    lines = remove_duplicate(get_lines_single_file(filename))
    map_result = map(lambda line: jieba.posseg.cut(line), lines)
    words = reduce(lambda left, right: list(left) + list(right), map_result)
    word_vec = []
    for word, tag in words:
        if word not in stop_words_set and re.match(r'n.*|v.*|a.*', tag) and not re.match(r'nr|ns|nz', tag):
            word_vec.append(word)
            # print word, tag_weight
    return word_vec


def get_sorted_lines():
    for i in range(8000):
        lines = remove_duplicate(get_lines_single_file('../../8000/' + str(i) + '.txt'))
        with open('../../8000_copy/' + str(i) + '.txt', 'w') as ofs:
            ofs.write('\n'.join(lines))


def get_words():
    for i in range(8000):
        words = get_words_single_file('../../8000/' + str(i) + '.txt')
        write_words = '\n'.join(words)
        write_words = write_words.encode('utf-8')
        with open('../../8000_words/' + str(i) + '.txt', 'w') as ofs:
            ofs.write(write_words)


init_stop_words_set(stop_file_name)
get_words()
get_sorted_lines()
