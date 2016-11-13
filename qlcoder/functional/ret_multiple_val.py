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

fib = \
    Y(lambda fact: \
          lambda n: \
              1 if n == 0 else fact(n - 1) * n)

print fib(5)
