import os
from PIL import Image

data_dir = os.path.abspath('.' + os.sep + 'datasets')
png_big_path = data_dir + os.sep + 'sift_big'
png_small_path = data_dir + os.sep + 'sift_small'

jpg_big_path = data_dir + os.sep + 'big'
jpg_small_path = data_dir + os.sep + 'realall'


def mkdir_if_not_exits():
    two_dir_list = [png_big_path, png_small_path]

    for ele in two_dir_list:
        if not os.path.exists(ele):
            os.mkdir(ele)


def walk_dir(walk_dir_path, des_dir_path):
    walk = os.walk(walk_dir_path)
    for root, dir, file_list in walk:
        for file_name in file_list:
            print root
            save_file_name = file_name.replace('.jpg', '.png')
            print file_name, save_file_name
            im = Image.open(root + os.sep + file_name)
            im.save(des_dir_path + os.sep + save_file_name)


mkdir_if_not_exits()
walk_dir(jpg_big_path, png_big_path)
walk_dir(jpg_small_path, png_small_path)
