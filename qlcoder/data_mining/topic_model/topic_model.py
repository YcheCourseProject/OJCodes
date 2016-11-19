#!/usr/bin/python
# coding:utf-8

import sys

reload(sys)
sys.setdefaultencoding("utf8")

import jieba
from gensim import corpora, models


def get_stop_words_set(file_name):
    with open(file_name, 'r') as file:
        return set([line.strip() for line in file])


def get_words_list(file_name, stop_word_file):
    stop_words_set = get_stop_words_set(stop_word_file)
    print "共计导入 %d 个停用词" % len(stop_words_set)
    word_list = []
    with open(file_name, 'r') as file:
        for line in file:
            tmp_list = list(jieba.cut(line.strip(), cut_all=False))
            # 注意这里term是unicode类型，如果不转成str，判断会为假
            word_list.append([term for term in tmp_list if str(term) not in stop_words_set])
    return word_list


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print "Usage: %s <raw_msg_file> <stop_word_file>" % sys.argv[0]
        sys.exit(1)

    raw_msg_file = sys.argv[1]
    stop_word_file = sys.argv[2]

    # 列表，其中每个元素也是一个列表，即每行文字分词后形成的词语列表
    word_list = get_words_list(raw_msg_file, stop_word_file)
    # 生成文档的词典，每个词与一个整型索引值对应
    word_dict = corpora.Dictionary(word_list)
    # 词频统计，转化成空间向量格式
    corpus_list = [word_dict.doc2bow(text) for text in word_list]
    lda = models.ldamodel.LdaModel(corpus=corpus_list, id2word=word_dict, num_topics=8, alpha='auto')

    output_file = './output_lda.txt'
    with open(output_file, 'w') as f:
        for pattern in lda.show_topics():
            print >> f, "%s" % str(pattern)
