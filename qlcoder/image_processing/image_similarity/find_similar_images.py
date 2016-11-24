#!/usr/bin/env python
from PIL import Image
import six
import imagehash
import os


def find_similar_images(user_path, hash_func=imagehash.average_hash):
    def is_image(filename):
        f = filename.lower()
        return f.endswith(".png") or f.endswith(".jpg") or \
               f.endswith(".jpeg") or f.endswith(".bmp") or f.endswith(".gif")

    image_file_names = [os.path.join(user_path, path) for path in os.listdir(user_path) if is_image(path)]
    images = {}
    for img in sorted(image_file_names):
        hash = hash_func(Image.open(img))
        images[hash] = images.get(hash, []) + [img]

    for k, img_list in six.iteritems(images):
        if len(img_list) > 1:
            print
            " ".join(img_list)
