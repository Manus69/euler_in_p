import elib

def _p12(n_div):
    t_gen = elib.trianglen_gen()
    next(t_gen)

    while True:
        tn = next(t_gen)
        if (elib.count_divisors(tn) >= n_div): return tn
    

def p12():
    print(_p12(500))
