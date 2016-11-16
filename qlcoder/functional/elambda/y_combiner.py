closure_name = \
    lambda x: \
        lambda y: \
            x + y

print closure_name(1)(2)

closure2_name = \
    lambda choice: \
        lambda x: \
            lambda y: \
                x * x if choice == 0 else y * y
print closure2_name(0)(1)(2)
print closure2_name(1)(1)(2)

Y = \
    lambda f: \
        (lambda x: f(lambda v: x(x)(v))) \
            (lambda x: f(lambda v: x(x)(v)))

fac_callable = \
    Y(lambda fact: \
          lambda n: \
              1 if n == 0 else fact(n - 1) * n)

print fac_callable(5)

ret = apply(lambda a, b, c: a + b if c == 0 else a - b, [1, 2, 3])
ret2 = apply(lambda a: a, [1])
print ret

with open('my_json_str.txt') as ifs:
    my_dict = eval(ifs.readline())
    for my_key in my_dict:
        print my_key, my_dict[my_key]