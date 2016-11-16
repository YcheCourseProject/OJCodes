;Y combiner
(define Y
  (lambda (f)
    ((lambda (x) (f (lambda (v) ((x x) v))))
       (lambda (x) (f (lambda (v) ((x x) v)))))))

;fast pow callable
(define fast_pow_callable
  (lambda (fast_pow)
    (lambda (a)
      (lambda (b)
        (cond
          ((< b 1) 1)
        (else
          (cond
            ((< b 2) a)
          (else (* ((fast_pow a)(/ b 2))
                    ((fast_pow a)(/ (+ b 1) 2)))))))))))

;number fast pow examples
(((Y fast_pow_callable) 2) 0)
(((Y fast_pow_callable) 2) 5)

;idx is either 0 or 1

(define fib_callable
  (lambda (fib_mat_pow)
   (lambda (pow_num)
    (lambda (idx)
     (cond
       ((< pow_num 2) 1)
     (else
       (((((lambda (a)(lambda (b)(lambda (ap)(lambda (bp)
              (cond
                ((< idx 1) (+ (* a ap) (* b bp)))
              (else
                (+ (* a bp) (* (b (- ap bp))))))))))
            ((fib_mat_pow (/ pow_num 2)) 0))
          ((fib_mat_pow (/ pow_num 2)) 1))
        ((fib_mat_pow (/ (+ pow_num 1) 2)) 0))
      ((fib_mat_pow (/ (+ pow_num 1) 2)) 1))))))))

(((Y fib_callable) 10) 0)
