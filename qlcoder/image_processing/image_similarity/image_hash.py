from PIL import Image
import imagehash
import os


def is_image(filename):
    f = filename.lower()
    return f.endswith(".png") or f.endswith(".jpg") or \
           f.endswith(".jpeg") or f.endswith(".bmp") or f.endswith(".gif")


def compute_image_hash_vals(path_info):
    ret_dict = {}
    dir_path = os.path.join(os.path.dirname(__file__))
    walk_image2 = os.walk(dir_path + '/../datasets/' + path_info)
    for root, dir, files in walk_image2:
        for file_name in files:
            if file_name.endswith('jpg') or file_name.endswith('png'):
                my_path = root + '/' + file_name
                ret_dict[int(file_name.split('.')[0])] = imagehash.average_hash(Image.open(my_path))
    return ret_dict


def compute_similar_bit_in_bool_arr(left, right):
    count = 0
    for i in range(len(left)):
        if left[i] == right:
            count += 1
    return count


image2_hash_dict = compute_image_hash_vals('image2')
image1_hash_dict = compute_image_hash_vals('image1')
image2_res_list = []
for i in range(len(image2_hash_dict)):
    tmp = image2_hash_dict[i + 1]
    tmp_idx = --1
    min = 99999
    for ele in image1_hash_dict:
        if abs(tmp - image1_hash_dict[ele]) < min:
            tmp_idx = ele
            min = abs(tmp - image1_hash_dict[ele])
    image2_res_list.append(tmp_idx)

print ','.join(map(str,image2_res_list))
print reduce(lambda left, right: left + right, image2_res_list)
# for i in range(len(image2_hash_dict)):
# print image2_hash_dict[i + 1]
