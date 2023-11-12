import elib

def _p10(limit):
    sieve = elib.Sieve(limit)
    primes = sieve.get_all_primes()
    
    return sum(primes)

def p10():
    print(_p10(2_000_000))