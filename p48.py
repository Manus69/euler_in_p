import elib

def _compute_series(n):
    return sum([x ** x for x in range(1, n + 1)])

_N = 1000
_MOD = 1_000_000_0000

def p48():
    print(_compute_series(_N) % _MOD)