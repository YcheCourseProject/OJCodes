# ~/anaconda2/bin/python
# coding:utf-8

import sys
import os

reload(sys)
sys.setdefaultencoding("utf8")
with open('./output_lda.txt') as ifs:
    strs = ifs.readlines()
    eval_str = ','.join(strs)
    eval_str = '[' + eval_str + ']'
    eval_res = eval(eval_str)
    # print eval_res
    for ele in eval_res:
        print ele[0],':',ele[1]
        # topic_words = map(lambda ele: str(ele[1]), eval_res)
