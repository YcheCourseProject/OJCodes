import numpy as np


def demo_numpy_usage():
    # matrix, vector
    my_matrix = [[1] * 3] * 3
    my_vec = [1] * 3
    my_vec = np.dot(my_vec, my_matrix)
    print 'result:' + ','.join(map(str, my_vec))

    # matrix
    my_matrix[0] = map(lambda x: x / reduce(lambda x, y: x + y, my_matrix[0], 0.0), my_matrix[0])
    print 'matrix:' + str(my_matrix)

    # matrix
    my_matrix1 = np.dot(my_matrix, my_matrix)
    print my_matrix1
    print np.multiply(my_matrix, my_matrix)


if __name__ == '__main__':
    demo_numpy_usage()
