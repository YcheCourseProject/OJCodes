import numpy as np


def yche_matrix_pow(a, b):
    if b == 1:
        return a
    else:
        return np.dot(yche_matrix_pow(a, b / 2), yche_matrix_pow(a, (b + 1) / 2))


def fib(n):
    primitive_matrix = np.matrix([[1, 1], [1, 0]])
    if n < 2:
        return n
    else:
        return yche_matrix_pow(primitive_matrix, n - 1).item(0, 0)


answer = ','.join([str(fib(i)) for i in range(43)])
print len(answer)
print answer

tmp=[0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597,2584,4181,6765,10946,17711,28657,46368,75025,121393,196418,317811,514229,832040,1346269,2178309,3524578,5702887,9227465,14930352,24157817,39088169,63245986,102334155,165580141]
print len(tmp)