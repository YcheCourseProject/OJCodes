import numpy as np
from sklearn.naive_bayes import GaussianNB

if __name__ == '__main__':
    training_arr = np.loadtxt('dataset/train0.txt', str, '#', ' ')
    testing_arr = np.loadtxt('dataset/check0.txt', str, '#', ' ')

    arr_y = map(lambda ele: int(ele[11]), training_arr)
    arr_x = map(lambda ele: map(lambda x: float(x), ele[1:10]), training_arr)
    testing_arr = map(lambda ele: map(lambda x: float(x), ele[1:10]), testing_arr)

    clf = GaussianNB()
    clf.fit(arr_x, arr_y)
    res_arr = clf.predict(testing_arr)

    print res_arr
    print ''.join(map(str, res_arr))
