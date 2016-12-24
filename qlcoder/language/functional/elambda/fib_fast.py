def pei_fib(n, ta, tb, a, b):
    if n < 1:
        return tb
    else:
        if n / 2 * 2 < n:
            return pei_fib(n / 2, a * ta + b * tb, b * ta + tb * (a - b), a * a + b * b, b * (2 * a - b))
        else:
            return pei_fib(n / 2, ta, tb, a * a + b * b, b * (2 * a - b))


def fib_by_pei(n):
    if n < 2:
        return n
    else:
        return pei_fib(n - 2, 1, 1, 1, 1)


def test_fib1():
    for i in range(20):
        print pei_fib(i, 1, 1, 1, 1)


def yche_fib(n, ta, tb, a, b):
    if n < 2:
        return ta * a + tb * b
    else:
        if n / 2 * 2 < n:
            return yche_fib(n / 2, (ta + tb) * a + ta * b, ta * a + tb * b, a * (a + 2 * b), a * a + b * b)
        else:
            return yche_fib(n / 2, ta, tb, a * (a + 2 * b), a * a + b * b)


def fib_by_che(n):
    if n < 2:
        return n
    else:
        return yche_fib(n, 1, 0, 1, 0)


# for i in range(10):
#     print fib_by_che(i)

test_fib1()