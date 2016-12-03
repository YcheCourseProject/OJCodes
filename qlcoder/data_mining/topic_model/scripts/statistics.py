# ~/anaconda2/bin/python
# coding:utf-8

count = 0
for i in range(8000):
    with open('../8000_words/' + str(i) + '.txt') as ifs:
        lines = ifs.readlines()
        lines = map(lambda line: line.strip(), lines)
        if len(lines) < 2:
            count += 1
            print i
            print ','.join(lines)

            competition_words = ['新华社', '照片', '体育', '足球', '冠军', '拜仁慕尼黑队', '球员', '获胜', '庆祝', '胜利', '拜仁慕尼黑队', '客场', '战平',
                                 '队', '提前', '夺得', '联赛', '冠军', '历史', '夺得', '联赛', '冠军', '新华社']
            with open('../8000_words/' + str(i) + '.txt', 'w') as ofs:
                ofs.writelines('\n'.join(competition_words))
print count
