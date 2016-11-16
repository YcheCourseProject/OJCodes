#lambda演算-1 -> Elambda 学习资料
##Elambda Y Combiner Skeleton
- skeleton code:

```scm
(\f.
  (\x.(f \v.((x x) v))
     \x.(f \v.((x x) v)))
       \recusive_function_name.
        \recursive_function_param.
          your_implementation_to_be_eval_as_a_number
))

```

- usage
上面代码的结果是一个operator，如果要求值，需要apply到参数上得到结果

##注意点
- 然后经过d师的指点，发现在cond分支中，对于`((mul n) (fact ((sub n) 1)))`，需要加上`\_.`，包装成lambda

##Python 解释Y combiner
- python中apply的语法与scheme和elambda差别比较大，是函数调用的语法

- python的Y combiner示例如下所示,(为了看起来更美观，`\`隔开一行的代码，python解释器会忽略掉它)：

```python
Y = \
    lambda f: \
        (lambda x: f(lambda v: x(x)(v))) \
            (lambda x: f(lambda v: x(x)(v)))

fac_callable = \
    Y(lambda fact: \
          lambda n: \
              1 if n == 0 else fact(n - 1) * n)

print fac_callable(5)
```

- 合起来写

```python
fac_callable2 = \
    (lambda f: \
         (lambda x: f(lambda v: x(x)(v))) \
             (lambda x: f(lambda v: x(x)(v)))) \
                (lambda fact: \
                     lambda n: \
                         1 if n == 0 else fact(n - 1) * n)

print fac_callable2(5)

```

##Scheme解释Y combiner
- 感觉scheme写出来比elambda更美观一点。。。

- Y combiner的解释

```scm
(define Y
  (lambda (f)
    ((lambda (x) (f (lambda (v) ((x x) v))))
       (lambda (x) (f (lambda (v) ((x x) v)))))))

((Y
   (lambda (fact)
      (lambda (n)
        (cond ((zero? n) 1)
          (else (* n (fact (1- n))))))))
5)
```

- 先把王垠的scheme fact代码拷贝过来, 外面是pattern部分 Y combiner, apply Y combiner 到 lambda上， apply完的东西再apply到5上面

```scm
(((lambda (f)
  ((lambda (x) (f (lambda (v) ((x x) v))))
   	(lambda (x) (f (lambda (v) ((x x) v))))))
		  (lambda (fact)
			(lambda (n)
			  (cond ((zero? n) 1)
				(else (* n (fact (1- n))))))))
5)

```

- 然后稍微修改一下

```scm
(((lambda (f)
  ((lambda (x) (f (lambda (v) ((x x) v))))
   	(lambda (x) (f (lambda (v) ((x x) v))))))
		  (lambda (fact)
			(lambda (n)
			  (cond ((< n 1) 1)
				(else (* n (fact (1- n))))))))
5)
```

##其它知识扩充
- python解释 currying手法

```python
closure_name = \
    lambda x: \
        lambda y: \
            x + y

print closure_name(1)(2)
```

- python解释 返回多个值

```
closure2_name = \
    lambda choice: \
        lambda x: \
            lambda y: \
                x * x if choice == 0 else y * y
print closure2_name(0)(1)(2)
print closure2_name(1)(1)(2)
```