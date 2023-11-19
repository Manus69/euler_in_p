import elib

def _is_triang(x):
    return elib.quadratic_root_p(1, 1, -2 * x).is_integer()

def _is_pentag(x):
    return elib.quadratic_root_p(3, -1, -2 * x).is_integer()

def _hex(n):
    return n * (2 * n - 1)

_START = 144

def _find_number(n_start):
    n = n_start
    while True:
        x = _hex(n)
        if _is_triang(x) and _is_pentag(x): return x
        n += 1

def p45():
    print(_find_number(_START))