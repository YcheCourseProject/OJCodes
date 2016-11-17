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


# for i in range(20):
#     print fib_by_pei(i)

# print fib_by_pei(1000000)

for i in range(20):
    print pei_fib(i, 2, 1, 1, 1)
