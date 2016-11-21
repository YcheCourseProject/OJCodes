# ~/anaconda2/bin/python
# coding:utf-8

import sys
from gensim import corpora, models, matutils
from sklearn.cluster import KMeans
import numpy

import data_preprocessing_util

reload(sys)
sys.setdefaultencoding("utf8")

if __name__ == '__main__':
    lst = []
    print len(lst)
    # 列表，其中每个元素也是一个列表，即每行文字分词后形成的词语列表
    word_list = data_preprocessing_util.return_all_key_words()
    print len(word_list)
    # 生成文档的词典，每个词与一个整型索引值对应
    word_dict = corpora.Dictionary(word_list)

    # 词频统计，转化成空间向量格式
    corpus_list = [word_dict.doc2bow(text) for text in word_list]
    print len(corpus_list)

    tfidf = models.TfidfModel(corpus_list)
    corpus_tfidf = tfidf[corpus_list]
    print len(corpus_tfidf)

    # 降低维度
    lda = models.ldamodel.LdaModel(corpus=corpus_list, id2word=word_dict, num_topics=30, alpha='auto')
    corpus_lda = lda[corpus_tfidf]

    for pattern in lda.show_topics():
        print 'topic', pattern[0], str(pattern[1])
    print len(lda.show_topics())

    kmean = KMeans(n_clusters=8)
    lda_matrix = matutils.corpus2csc(corpus_lda).transpose()
    kmean.fit(lda_matrix)

    res = kmean.predict(lda_matrix)
    print res
    with open('output_tmp_res.txt', 'w') as ofs:
        print len(res)
        ofs.write('[' + ','.join(map(str, res)) + ']')
