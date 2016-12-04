# ~/anaconda2/bin/python
# coding:utf-8

tag_word_dict = dict()
with open('frequency_top_1000.txt') as ifs:
    lines = ifs.readlines()
    for line in lines:
        info = line.rstrip().split(' ')
        if len(info) > 2:
            word = info[0]
            tag = info[2]
            if tag not in tag_word_dict:
                tag_word_dict[tag] = []
            tag_word_dict[tag].append(word)

    print len(tag_word_dict)
    for tag in tag_word_dict:
        print tag, len(tag_word_dict[tag])
        # print tag_word_dict[tag_weight]


def get_tag_dict(word_list, tag_word_dict):
    tuple_dict = dict()
    for word in word_list:
        for tag in tag_word_dict:
            if word in tag_word_dict[tag]:
                if tag not in tuple_dict:
                    tuple_dict[tag] = 0
                tuple_dict[tag] += 1
    return tuple_dict


def pretty_dict(my_tag_dict):
    str_list = []
    for tag in my_tag_dict:
        str_list.append(tag + '@' + str(my_tag_dict[tag]))
    return ','.join(str_list)


with open('output_readable.txt') as ifs:
    lines = ifs.readlines()
    data_list = map(lambda ele: ele.rstrip().split(' '), lines)
    data_list = map(lambda ele: [ele[0].split(':')[1], ele[1].split(':')[1].split(',')], data_list)
    data_list = map(lambda ele: [ele[0], ele[1], get_tag_dict(ele[1], tag_word_dict)], data_list)
    okay_tag = 0
    with open('output_readable_taged.txt', 'w') as ofs:
        for data in data_list:
            my_lst = ['question:' + str(data[0]), 'data:' + ','.join(data[1]), 'tags:' + pretty_dict(data[2])]

            if len(data[2]) >= 1:
                okay_tag += 1
            else:
                print ' '.join(my_lst)

            ofs.write(' '.join(my_lst) + '\n')

    print okay_tag
