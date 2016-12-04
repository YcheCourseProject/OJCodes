# ~/anaconda2/bin/python
# coding:utf-8


# with open('tmp.txt') as line_ifs:
#     ref_words = line_ifs.readlines()

import operator

my_dict = {
    0: '教育',
    1: 'IT',  # ..
    2: '文化',
    3: '旅游',
    4: '体育',
    5: '健康',
    6: '财经',
    7: '军事'
}

qlcoder_dict = {
    'IT': 1,
    '健康': 2,
    '体育': 3,
    '旅游': 4,
    '教育': 5,
    '文化': 6,
    '军事': 7,
    '财经': 8

}


def get_frequency_dict(words):
    frequency_dict = dict()
    for word in words:
        if word not in frequency_dict:
            frequency_dict[word] = 0
        frequency_dict[word] += 1

    sorted_x = sorted(frequency_dict.items(), key=operator.itemgetter(1))[::-1]
    return map(lambda ele: ele[0], sorted_x)


def get_word_list():
    word_list = []
    for i in range(8000):
        with open('../../8000_words/' + str(i) + '.txt') as ifs:
            lines = ifs.readlines()
            lines = map(lambda line: line.strip(), lines)
            word_list.append(get_frequency_dict(lines))
    return word_list


with open('output_tmp_res.txt') as my_ifs:
    eval_str = my_ifs.readline()
    mark_lst = eval(eval_str)
    label = []
    category_words = [[] for i in range(8)]
    word_list = get_word_list()

    for i in range(8000):
        label.append(qlcoder_dict[my_dict[mark_lst[i]]])
        category_words[mark_lst[i]].extend(word_list)
        # if mark_lst[i] == 7:
        #     with open('../../8000_words/' + str(i) + '.txt') as ifs:
        #         print str(i) + ','.join(map(lambda line: line.strip(), ifs.readlines()))
        #         label = map(str, label)

    label = map(str, label)
    print len(label)
    print '[' + ','.join(label) + ']'

    print len(category_words)
    idx=0
    for category in category_words:
        print len(category), my_dict[idx]
        idx+=1
    # category_words = map(lambda category: get_frequency_dict(category), category_words)
