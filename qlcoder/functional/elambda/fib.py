import numpy as np


def pei_fib(n, ta, tb, a, b):
    if n == 0:
        return tb
    if n & 1:
        return pei_fib(n / 2, a * ta + b * tb, b * ta + tb * (a - b), a * a + b * b, b * (2 * a - b))
    return pei_fib(n / 2, ta, tb, a * a + b * b, b * (2 * a - b))


# if number of bits is odd, we multiply a
def q_pow(a, b):
    t = 1
    while b > 0:
        if b & 1:
            t *= a
        a = a * a
        b /= 2
    return t


def yche_pow(a, b):
    if b == 0:
        return 1
    if b == 1:
        return a
    else:
        return yche_pow(a, b / 2) * yche_pow(a, (b + 1) / 2)


def yche_matrix_pow(a, b):
    if b == 1:
        return a
    else:
        return np.dot(yche_pow(a, b / 2), yche_pow(a, (b + 1) / 2))


def fib(n):
    primitive_matrix = np.matrix([[1, 1], [1, 0]])
    if n < 2:
        return n
    else:
        return yche_matrix_pow(primitive_matrix, n - 1).item(0, 0)


def naive_fib(n):
    if n < 2:
        return n
    else:
        return naive_fib(n - 1) + naive_fib(n - 2)


def fib_mat_pow(pow_num, idx):
    if pow_num < 2:
        return 1
    else:
        a = fib_mat_pow(pow_num / 2, 0)
        b = fib_mat_pow(pow_num / 2, 1)
        a_plus = fib_mat_pow((pow_num + 1) / 2, 0)
        b_plus = fib_mat_pow((pow_num + 1) / 2, 1)
        if idx < 1:
            return a * a_plus + b * b_plus
        else:
            return a * b_plus + b * a_plus - b * b_plus


def fast_fib(idx):
    if idx < 2:
        return idx
    else:
        return fib_mat_pow(idx - 1, 0)


print q_pow(2, 4)
print yche_pow(2, 4)
print yche_pow(2, 5)
print yche_pow(2, 0)

print fib(10)
print naive_fib(10)
print 'fib demo:'
for i in range(12):
    print fast_fib(i),
