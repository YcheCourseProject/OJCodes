# ~/anaconda2/bin/python
# coding:utf-8

import sys
import os
import re
import jieba.analyse

reload(sys)
sys.setdefaultencoding("utf8")

stop_words_set = {}
stop_file_name = 'cn_stop_words.txt'
res_output_file_name = 'output_whole_corpus.txt'
res_output_all_words_file_name = 'output_all_words.txt'
bad_info_file_name = 'output_bad_info.txt'


def init_stop_words_set(file_name):
    global stop_words_set
    with open(file_name, 'r') as file:
        stop_words_set = {' '} | set([line.strip() for line in file])


def generate_whole_corpus_file():
    with open(res_output_all_words_file_name, 'w') as ofs_all:
        with open(res_output_file_name, 'w') as ofs:
            walk = os.walk('./8000')
            line_list = {}
            all_words_list = []
            for root, dir, files in walk:
                for file_name in files:
                    my_path = root + '/' + file_name
                    if '.txt' in file_name:
                        line_list[file_name.rstrip('.txt')] = extract_key_words(my_path)
                        all_words_list.append(extract_all_words(my_path))
            ofs.write(str(line_list))
            ofs_all.write(str(all_words_list))


def is_filtered_pattern(your_str):
    your_str = str(your_str)
    if re.match('[0-9]+', your_str):
        return True
    if re.match('[a-zA-Z]+', your_str):
        return True
    if your_str in stop_words_set:
        return True
    if re.match('.*[\r|\n]].*', your_str):
        return True
    if re.match('.* .*', your_str):
        return True


def extract_key_words(input_file_name):
    with open(input_file_name) as ifs:
        lines = ifs.readlines()
        line = '\n'.join(lines)
        key_words = jieba.analyse.extract_tags(line, topK=20)
        # print key_words
        key_words = filter(lambda ele: not is_filtered_pattern(ele), key_words)
        return key_words


def extract_all_words(input_file_name):
    with open(input_file_name) as ifs:
        lines = ifs.readlines()
        ret_all_words = []
        for line in lines:
            all_words = jieba.analyse.extract_tags(line, topK=15)
            all_words = filter(lambda ele: not is_filtered_pattern(ele), all_words)
            ret_all_words.extend(all_words)
        return ret_all_words


def read_file_get_dict():
    with open(res_output_file_name) as ifs:
        eval_str = ifs.readline()
        my_dict = eval(eval_str)
        return my_dict


def find_bad_things():
    my_dict = read_file_get_dict()
    bad_list = []
    with open('output_readable.txt', 'w') as readable_ofs:
        with open(bad_info_file_name, 'w') as ofs:
            for i in range(8000):
                if len(my_dict[str(i)]) < 10:
                    tmp_str = 'question:' + str(i) + ' data:' + ','.join(my_dict[str(i)]) + 'data length:' + str(
                        len(my_dict[str(i)])) + '\n'
                    bad_list.append(str(i))
                    ofs.write(tmp_str)
                else:
                    readable_ofs.write('question:' + str(i) + ' data:' + ','.join(my_dict[str(i)]) + '\n')

    return set(bad_list)


def return_all_key_words():
    my_dict = read_file_get_dict()
    words_list = []
    for ele in my_dict:
        words_list.append(my_dict[ele])
    return words_list


def return_useful_words_list():
    my_dict = read_file_get_dict()
    bad_set = find_bad_things()
    words_list = []
    for ele in my_dict:
        if ele not in bad_set:
            words_list.append(my_dict[ele])
    return words_list


def return_all_words():
    with open(res_output_all_words_file_name) as ifs:
        eval_str = ifs.readline()
        arr = eval(eval_str)
        return arr


if __name__ == '__main__':
    init_stop_words_set(stop_file_name)
    generate_whole_corpus_file()
    filtered_word_list = return_useful_words_list()
    print len(filtered_word_list)
