import hashlib

if __name__ == '__main__':
    print hashlib.md5("").hexdigest()
    print hashlib.md5().hexdigest()

    my_str = str()
    # with open('time_line_res.txt') as fs:
    #     my_str = fs.readline()

    print len(my_str)
    md5str = hashlib.md5(my_str[1:len(my_str)]).hexdigest()
    print md5str
    print len(md5str)

    print hashlib.md5('a').hexdigest()
    print hashlib.md5('abcdefghijklmnopqrstuvwxyz').hexdigest()
