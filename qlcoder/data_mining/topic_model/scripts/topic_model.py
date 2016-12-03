# ~/anaconda2/bin/python
# coding:utf-8

from gensim import corpora, models, matutils
from sklearn.cluster import KMeans

if __name__ == '__main__':
    word_list = []
    for i in range(8000):
        with open('../8000_words/' + str(i) + '.txt') as ifs:
            lines = ifs.readlines()
            lines = map(lambda line: line.strip(), lines)
            word_list.append(lines)
    # 列表，其中每个元素也是一个列表，即每行文字分词后形成的词语列表
    # word_list = data_preprocessing_util.return_all_key_words()
    print len(word_list)

    # 生成文档的词典，每个词与一个整型索引值对应
    word_dict = corpora.Dictionary(word_list)

    # 词频统计，转化成空间向量格式
    corpus_list = [word_dict.doc2bow(text) for text in word_list]
    print len(corpus_list)

    # Tfidf模型 计算对应空间向量
    tfidf = models.TfidfModel(corpus_list)
    corpus_tfidf = tfidf[corpus_list]
    print len(corpus_tfidf)

    # LDA, 降低维度
    lda = models.ldamodel.LdaModel(corpus=corpus_tfidf, id2word=word_dict, num_topics=50, alpha='auto')
    corpus_lda = lda[corpus_tfidf]
    print 'finish lda'

    # K-means, 聚类
    kmean = KMeans(n_clusters=8, n_jobs=-1)
    lda_matrix = matutils.corpus2csc(corpus_lda).transpose()
    kmean.fit(lda_matrix)
    res = kmean.predict(lda_matrix)
    print res

    with open('output_tmp_res.txt', 'w') as ofs:
        print len(res)
        ofs.write('[' + ','.join(map(str, res)) + ']')
