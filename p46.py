import elib
import math

_PRIME_LIMIT = 1_000_000

def _check_if_square(x):
    return math.sqrt(x / 2).is_integer()

def _check(x, primes_lt : list) -> bool:
    idx = 0
    while primes_lt[idx] < x:
        rem = x - primes_lt[idx]
        if _check_if_square(rem): return True
        idx += 1
    
    return False

def p46():
    sieve = elib.Sieve(_PRIME_LIMIT)
    primes = sieve.get_all_primes()
    odds = [x for x in range(3, _PRIME_LIMIT, 2) if not sieve.is_prime(x)]

    for x in odds:
        if not _check(x, primes):
            print(x)
            break