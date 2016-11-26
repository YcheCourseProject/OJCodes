# ~/anaconda2/bin/python
# coding:utf-8

import re


def check_error():
    with open('/home/cheyulin/GitRepos/OJCodes/qlcoder/database/query/tuple_query/build/tmp.txt') as ifs:
        lines = ifs.readlines()
        to_used = lines[15: 15 + 13262]
        to_used = map(lambda ele: ele.lstrip().rstrip(), to_used)
        my_set = set()
        my_list = [-1]
        for ele in to_used:
            # print ele
            if not ('拉链' in ele or '其他' in ele):
                print 'bad'
                break
            tmp = ele.split(', ')
            sale_num = int(tmp[2])
            created_at = long(tmp[7])
            dsr = float(tmp[8])
            id = long(tmp[0][1:])
            my_set.add(id)
            my_list.append(id)
            print long(tmp[0][1:])
            if not (8468 <= sale_num <= 20576 and 1400703171 <= created_at <= 1442106921 and 3.7 <= dsr <= 4.6):
                print 'bad'
                break

        print '\n'
        print 'len', len(to_used), len(my_set)
        print 'first:', to_used[0]
        print 'query string:', lines[14]

        for i in range(1, len(to_used)):
            if my_list[i] == my_list[i - 1]:
                print my_list[i], i


if __name__ == '__main__':
    tagStr = "印花 新款 秋冬 纯色 字母 套装 套头 宽松 连帽 拼接 显瘦 拉链 条纹 " \
             "加厚 修身 收腰 情侣 大码 撞色 加绒 清新 休闲 文艺 甜美 运动 学院 韩系 " \
             "街头 通勤 OL 欧美 卡通 森系 复古 轻熟 民族 田园 简约 可爱 个性 聚酯纤维 涂层布 " \
             "涤纶 毛呢布 锦纶 其他 迷彩布 聚酯 羊皮立领 双层领 堆堆领 连帽 翻领 其他 可脱卸帽 " \
             "V领 圆领 口袋 拼接 品牌LOGO 拉链 系带 绣花 带毛领 字母 绑带 纽扣"
    tag = tagStr.split(" ")
    tag_set = set()
    for ele in tag:
        tag_set.add(ele)
    for ele in tag_set:
        for ele2 in tag_set:
            if ele != ele2 and ele in ele2:
                print ele, ele2
    print len(tag_set)
