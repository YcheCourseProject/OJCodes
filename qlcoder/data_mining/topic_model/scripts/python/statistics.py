# ~/anaconda2/bin/python
# coding:utf-8

import operator

competition_key_word = ['足球', '篮球', '羽毛球', '客场', '主场', '队员', '联赛', '比赛', '棋手', '棋赛']
competition_file_name = 'competition.txt'

finance_key_word = ['上涨', '大盘', '股市', '指数', '投资']
finance_file_name = 'finance.txt'


def extract_key_words(file_name, key_words):
    count = 0
    for i in range(8000):
        with open('../8000_words/' + str(i) + '.txt') as ifs:
            lines = ifs.readlines()
            lines = set(map(lambda line: line.strip(), lines))
            one_line = ','.join(lines)

            for key_word in key_words:
                if key_word in one_line:
                    count += 1
                    with open(file_name, 'a') as ofs:
                        tmp_lst = [str(i), one_line]
                        ofs.write(' '.join(tmp_lst) + '\n')
                    break
    print count


def cal_frequency(word_list):
    frequency_dict = dict()
    for words in word_list:
        for word in words:
            if word not in frequency_dict:
                frequency_dict[word] = 0
            frequency_dict[word] += 1
    print len(frequency_dict)
    sorted_x = sorted(frequency_dict.items(), key=operator.itemgetter(1))[::-1]
    return sorted_x


def extract_statistics(filename):
    with open(filename) as ifs:
        lines = ifs.readlines()
        lines = map(lambda line: line.strip().split()[1].split(','), lines)
        word_list = []
        for line in lines:
            word_list.append(line)

        sorted_pair = cal_frequency(word_list)
        print len(sorted_pair)

        with open('frequency_top_word_' + filename + '.txt', 'a') as ofs:
            for i in range(200):
                ofs.write(' '.join([sorted_pair[i][0], str(sorted_pair[i][1])]) + '\n')


extract_key_words(finance_file_name, finance_key_word)
