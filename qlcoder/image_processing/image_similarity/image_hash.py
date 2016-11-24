from PIL import Image
import imagehash
import os


def is_image(filename):
    f = filename.lower()
    return f.endswith(".png") or f.endswith(".jpg") or \
           f.endswith(".jpeg") or f.endswith(".bmp") or f.endswith(".gif")


def compute_image2_hash_vals():
    ret_dict = {}
    dir_path = os.path.join(os.path.dirname(__file__))
    walk_image2 = os.walk(dir_path + '/../datasets/image2')
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


image2_hash_dict = compute_image2_hash_vals()
for i in range(len(image2_hash_dict)):
    print image2_hash_dict[i + 1]
