#!/usr/bin/python
# -*- coding:utf8 -*-

import os
import time
import re
import jieba.analyse


def post_cut(url):
    fr = open(url + "/post_data.txt")
    fo = open(url + "/post_key.txt", "a+")
    for line in fr.readlines():
        term = line.strip().split("\t")
        if len(term) == 3 and term[2] != "":
            key_list = jieba.analyse.extract_tags(term[2], 30)  # get keywords
            ustr = term[0] + "\t"
            for i in key_list:
                ustr += i.encode("utf-8") + " "
            fo.write(ustr + "\n")
    fr.close()
    fo.close()


def post_tfidf(url):
    from sklearn.feature_extraction.text import HashingVectorizer
    fr = open(url + "/post_key.txt")
    id_list = []
    data_list = []
    for line in fr.readlines():
        term = line.strip().split("\t")
        if len(term) == 2:
            id_list.append(term[0])
            data_list.append(term[1])

    hv = HashingVectorizer(n_features=10000, non_negative=True)  # 该类实现hash技巧
    post_tfidf = hv.fit_transform(data_list)  # return feature vector 'fea_train' [n_samples,n_features]
    print 'Size of fea_train:' + repr(post_tfidf.shape)
    print post_tfidf.nnz
    post_cluster(url, id_list, post_tfidf)


def post_cluster(url, id, tfidf_vec):
    from sklearn.cluster import KMeans
    kmean = KMeans(n_clusters=300)
    print "kmeans"
    kmean.fit(tfidf_vec)
    #     pred = kmean.transform(tfidf_vec)

    #   count1 = 0
    #   count2 = 0
    #     pred_str = []
    #
    #     for item in pred:
    #         count1 += 1
    #         vec = ""
    #         for tmp in item :
    #             vec += str(tmp)[0:7] + "\t"
    #         pred_str.append(vec)
    #
    #     print len(pred_str)
    #     print len(id)

    pred = kmean.predict(tfidf_vec)
    fo = open(url + "/cluster.txt", "a+")
    for i in range(len(pred)):
        count2 += 1
        fo.write(id[i] + "\t" + str(pred[i]) + "\n")
    fo.close()
    print "%d+%d" % (count1, count2)


def post_lda(url, cluster):
    from gensim import corpora, models, matutils
    count = 0
    fr = open(url + "/post_key.txt")
    fo2 = open(url + "/post_vec_lda.txt", "a+")
    id_list = []
    data_list = []

    for line in fr.readlines():
        term = line.strip().split("\t")
        if len(term) == 2:
            count += 1
            id_list.append(term[0])
            word = term[1].strip().split()
            data_list.append(word)
    print "lda"
    dic = corpora.Dictionary(data_list)  # 构造词典
    corpus = [dic.doc2bow(text) for text in data_list]  # 每个text 对应的稀疏向量
    tfidf = models.TfidfModel(corpus)  # 统计tfidf
    print "lda"
    corpus_tfidf = tfidf[corpus]  # 得到每个文本的tfidf向量，稀疏矩阵
    lda = models.LdaModel(corpus_tfidf, id2word=dic, num_topics=200)
    corpus_lda = lda[corpus_tfidf]  # 每个文本对应的LDA向量，稀疏的，元素值是隶属与对应序数类的权重
    print "lda"

    num = 0
    for doc in corpus_lda:
        wstr = ""
        for i in range(len(doc)):
            item = doc[i]
            wstr += str(item[0]) + "," + str(item[1])[0:7] + "/"
        fo2.write(id_list[num] + "\t" + wstr[0:-1] + "\n")
        num += 1
    fr.close()
    fo2.close()
    print num

    if cluster:
        lda_csc_matrix = matutils.corpus2csc(corpus_lda).transpose()  # gensim sparse matrix to scipy sparse matrix
        post_cluster(url, id_list, lda_csc_matrix)


if __name__ == "__main__":
    url = "path"
    time = time.time()
    post_cut(url)
    post_tfidf(url)
    lda_cluster = False
    post_lda(url, lda_cluster)

    print time.time() - time