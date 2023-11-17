import elib
import math

_f_table = [math.factorial(x) for x in range(10)]

def _digit_fsum(x):
    return  sum([_f_table[d] for d in elib.to_digits(x)])

_LIMIT = 1_000_000

def _find_numbers(limit):
    f = lambda x: _digit_fsum(x) == x
    return [x for x in range(3, limit) if f(x)]

def p34():
    print(sum(_find_numbers(_LIMIT)))