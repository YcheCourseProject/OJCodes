(((lambda (f)
  ((lambda (x) (f (lambda (v) ((x x) v))))
   (lambda (x) (f (lambda (v) ((x x) v))))))
  (lambda (fact)
    (lambda (n)
      (cond ((zero? n) 1)
        (else (* n (fact (1- n))))))))
5)


(((lambda (f)
  ((lambda (x) (f (lambda (v) ((x x) v))))
   (lambda (x) (f (lambda (v) ((x x) v))))))
  (lambda (fact)
    (lambda (n)
      (cond ((< n 1) 1)
        (else (* n (fact (1- n))))))))
5)

(((lambda (f)
  ((lambda (x) (f (lambda (v) ((x x) v))))
   (lambda (x) (f (lambda (v) ((x x) v))))))
  (lambda (fact)
    (lambda (n)
      (cond ((< n 1) 1)
        (else (* n (fact (- n 1))))))))
5)

(define yche
  ((lambda (f)
    ((lambda (x) (f (lambda (v) ((x x) v))))
     (lambda (x) (f (lambda (v) ((x x) v))))))
    (lambda (fact)
      (lambda (n)
        (cond ((< n 1) 1)
          (else (* n (fact (- n 1)))))))))
