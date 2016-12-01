import data_preprocessing_util as yche_util
import os

my_list = []
for i in range(8000):
    my_list.append(yche_util.extract_all_words('8000' + os.sep + str(i) + '.txt'))

new_list = []
for ele in my_list:
    new_list.append(ele)

new_list = set(new_list)
print len(new_list)
