import elib
import collections

def _rot(dq : collections.deque):
    digit = dq.popleft()
    dq.append(digit)

def _collect(dq : collections.deque) -> int:
    number = 0
    for n in range(len(dq)):
        number *= 10
        number += dq[n]

    return number

def _check_even_digits(digits : list) -> bool:
    for d in digits: 
        if d % 2 == 0: return True

    return False

def _is_circular(prime, sieve : elib.Sieve):
    if prime == 2: return True

    digits = elib.to_digits(prime)
    if _check_even_digits(digits): return False

    digits = collections.deque(digits)
    for k in range(len(digits)):
        _rot(digits)
        if not sieve.is_prime(_collect(digits)): return False

    return True

def _get_all_circular(limit):
    sieve = elib.Sieve(limit)
    primes = sieve.get_primes_lt(limit)
    primes = [p for p in primes if _is_circular(p, sieve)]

    return primes

_N = 1_000_000

def p35():
    print(len(_get_all_circular(_N)))
