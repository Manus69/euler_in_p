import elib
import random

_N = 1_000_000

def p24():
    vals = list(range(10))
    perm = elib.Permutation(vals)

    for k in range(_N - 1): next(perm)
    
    print(perm.vals)