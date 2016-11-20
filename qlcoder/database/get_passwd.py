with open('passwd.txt')as ifs:
    lines=ifs.readlines()
    lines=filter(lambda ele:True if 'sucess' in ele else False, lines)
    chs=map(lambda ele:ele.split()[1],lines)
    print ''.join(chs)