# ~/anaconda2/bin/python
# coding:utf-8


# with open('tmp.txt') as line_ifs:
#     ref_words = line_ifs.readlines()

my_dict = {
    0: '旅游',
    1: 'IT',
    2: '财经',
    3: '健康',
    4: '体育',
    5: '军事',
    6: '文化',
    7: '教育'
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

with open('output_tmp_res.txt') as my_ifs:
    eval_str = my_ifs.readline()
    mark_lst = eval(eval_str)
    label = []
    for i in range(8000):
        label.append(qlcoder_dict[my_dict[mark_lst[i]]])
        if mark_lst[i] == 3:
            with open('../8000_words/' + str(i) + '.txt') as ifs:
                print str(i) + ','.join(map(lambda line: line.strip(), ifs.readlines()))
    label = map(str, label)
    print ''.join(label)
