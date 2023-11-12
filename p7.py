import elib

def _p7(n: int) -> int:
    sieve = elib.Sieve(n)
    return sieve.get_n_primes(n)[-1]

def p7():
    print(_p7(10_001))