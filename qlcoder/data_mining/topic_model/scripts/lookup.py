# ~/anaconda2/bin/python
# coding:utf-8


with open('tmp.txt') as line_ifs:
    ref_words = line_ifs.readlines()

    with open('output_tmp_res.txt') as my_ifs:
        eval_str = my_ifs.readline()
        mark_lst = eval(eval_str)
        for i in range(8000):
            if mark_lst[i] == 1:
                print ref_words[i]
