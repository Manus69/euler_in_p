import elib

def _p25(n_digits):
    fg = elib.fib_gen()
    idx = 0

    while True:
        x = next(fg)
        if elib.count_digits(x) >= n_digits: return idx
        idx += 1

_N = 1000
def p25():
    print(_p25(_N))