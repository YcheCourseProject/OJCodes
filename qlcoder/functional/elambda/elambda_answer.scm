(\f.
  (\x.(f \v.((x x) v))
     \x.(f \v.((x x) v)))
\fib_mat_pow.
 \pow_num.
   \idx.
    (((cond ((less pow_num) 2))
          \_.1)
          \_.((((\a.\b.\ap.\bp.
           (((cond ((less idx) 1))
               \_.((add ((mul a) ap))((mul b) bp)))
               \_.((add ((mul a)bp))((mul b)((sub ap)bp))))
            ((fib_mat_pow ((div pow_num) 2)) 0))
            ((fib_mat_pow ((div pow_num) 2)) 1))
            ((fib_mat_pow ((div ((add pow_num) 1)) 2)) 0))
            ((fib_mat_pow ((div ((add pow_num) 1)) 2)) 1)))
)
