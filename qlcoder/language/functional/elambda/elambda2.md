##前言
- 先挖个坑，之后来个scheme版本的代码，哈哈

##方法：这道题目很特殊
- 使用pei师所说的用两个数来表示矩阵，初始值是确定的  `1` 和 `1`， 从矩阵`[[1,1],[1,0]]`中取出来，`matrix[0][0]`表示大数，`matrix[0][1]`和`matrix[1][0]`表示中数，`matrix[1][1]= matrix[0][0]-matrix[0][1]`

- 看了下面的python脚本应该就可以明白解法了，因为我们的矩阵实在是太特殊了，我一开始还想写个矩阵的快速幂，后来发现完全没必要。。。

```python
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
    return idx if idx < 2 else fib_mat_pow(idx - 1, 0)

```

- 使用

```python
for i in range(12):
    print fast_fib(i),
```

- 结果

```
0 1 1 2 3 5 8 13 21 34 55 89
```

##Scheme实现
###基本知识
- scheme的解释器用的是 `guile`，交互式地把代码复制过去解释执行

- Y combiner实现

```scm
(define Y
  (lambda (f)
    ((lambda (x) (f (lambda (v) ((x x) v))))
       (lambda (x) (f (lambda (v) ((x x) v)))))))
```

###一个数的快速幂
- 一个数的快速幂实现(用一下宏定义)， `a^b`， 下面测试了一下`2^0`和`2^5`

```scm
(define fast_pow_callable
  (lambda (fast_pow)
    (lambda (a)
      (lambda (b)
        (cond ((< b 1) 1)
          (else (cond ((< b 2) a)
                  (else (* ((fast_pow a)
                              (/ b 2))
                           ((fast_pow a)
                              (/ (+ b 1) 2)) )))))))))

(((Y fast_pow_callable) 2) 0)
(((Y fast_pow_callable) 2) 5)
```

- 一个数的快速幂实现(写到一行里面去，不用宏定义)， `a^b`， 下面测试了一下`2^0`和`2^5`

```scm
((((lambda (f)
    ((lambda (x) (f (lambda (v) ((x x) v))))
       (lambda (x) (f (lambda (v) ((x x) v))))))
         (lambda (fast_pow)
           (lambda (a)
             (lambda (b)
               (cond ((< b 1) 1)
                 (else (cond ((< b 2) a)
                         (else (* ((fast_pow a)
                                     (/ b 2))
                                  ((fast_pow a)
                                     (/ (+ b 1) 2)) ))))))))
) 2) 0)

((((lambda (f)
    ((lambda (x) (f (lambda (v) ((x x) v))))
       (lambda (x) (f (lambda (v) ((x x) v))))))
         (lambda (fast_pow)
           (lambda (a)
             (lambda (b)
               (cond ((< b 1) 1)
                 (else (cond ((< b 2) a)
                         (else (* ((fast_pow a)
                                     (/ b 2))
                                  ((fast_pow a)
                                     (/ (+ b 1) 2)) ))))))))
) 2) 5)
```

##上一题的学习内容
- **Ycombiner** 的解释说明: 
	- Y apply 到 lambda
	- 然后出来的结果再 apply 到 单个参数

- scheme代码示例如下

```scheme
(define Y
  (lambda (f)
    ((lambda (x) (f (lambda (v) ((x x) v))))
     (lambda (x) (f (lambda (v) ((x x) v)))))))

((Y (lambda (fact)
      (lambda (n)
        (cond ((zero? n) 1)
          (else (* n (fact (1- n))))))))
5)
```

- **elambda vs Scheme**: d师把scheme中的定义lambda的语法改了一下，然后必须要用柯林化来实现多参数函数, apply 还是一样的 `(operator param0)`，只不过只能有一个参数在 elambda 中。 改动的lambda定义部分：在scheme中， `(lambda (x) (expression))`；在elambda中 ，`\x.expression `。

##这一题的学习内容
###矩阵快速幂

- 矩阵快速幂解决fib(n)
	- 感谢 [知乎的一个相关博客](https://zhuanlan.zhihu.com/p/19768646)
	- 推导过程大家可点链接看看，根据这个博客看出我们要用要算一个 `2 x 2` 的矩阵，具体推导过程可以看ik的，也可以去看看知乎的博客, 要计算的东西如下图所示
	
![](http://www.qlcoder.com//uploads/265cf5a319/147757352077320.jpg)

- 要用矩阵快速幂算的东西如下图
	
![](http://www.qlcoder.com//uploads/265cf5a319/147757515785663.jpg)

- 矩阵快速幂算法部分，解题重点
	- 也就是说`2 x 2` 矩阵的值中有三个是我们需要的 `matrix[0][1]` 和 `matrix[1][0]` 为 `fib(n+1)`, `matrix[0][0]`为 `fib(n+2)`， `matrix[1][1]` 为 `fib(n)`， 比如一开始`n=0`， 那么矩阵就是 `[[1,1], [1,0]]`

- 为了加深大家理解，首先整数的快速幂递归形式python代码， 矩阵的快速幂形式的时间复杂度的大致原理同整数快速幂

```python
def yche_pow(a, b):
    if b == 0:
        return 1
    if b == 1:
        return a
    else:
        return yche_pow(a, b / 2) * yche_pow(a, (b + 1) / 2)
```

```python
print yche_pow(2, 5)
```

- 矩阵的快速幂求fib(n)，下面的实现不是最正确/简洁的解题方法，仅仅为了说明矩阵快速幂的求解思路

```python
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
```

```python
print fib(10)
```

###函数式编程

- 函数式编程部分，柯林化

柯林化的学习主要可以参考的王垠的 [谈谈curring](http://www.yinwang.org/blog-cn/2013/04/02/currying)，是一种比较简单的手法，主要是因为函数是第一公民，可以作为参数和返回值。用单参数模拟多参数，引用下王垠的scheme代码。我们使用时候需要把f apply到第一个参数，返回一个匿名函数xxx，然后再把xxx apply 到第二个参数上。

```scheme
(define f
  (lambda (x)
    (lambda (y)
      (+ x y))))
```

-  函数式编程部分，尾递归

- 函数式编程部分，中间结果存在哪里

这里没有heap给我们用，那么我们只能把中间结果放在函数的调用栈里面了。函数式编程就是这样，你要搞个局部变量也要来一个lambda包装起来，然后capture值。
