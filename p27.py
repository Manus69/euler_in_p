import elib

_A = 999
_B = 1000

def _coeff_product(a, b):
    return a * b

def _eval(a, b, x):
    return x * x + a * x + b

def _count_primes(a, b, sieve: elib.Sieve):
    n = 0
    for x in range(abs(b)):
        if not sieve.is_prime(_eval(a, b, x)): break
        n += 1
    
    return n

def _find_max(sieve: elib.Sieve):
    max_a, max_b, max_n = 0, 0, 0

    for a in range(- _A, _A + 1):
        for b in range(- _B, _B + 1):
            current = _count_primes(a, b, sieve)
            if current > max_n: max_a, max_b, max_n = a, b, current
    
    return _coeff_product(max_a, max_b)

def p27():
    sieve = elib.Sieve(_A * _B)
    print(_find_max(sieve))