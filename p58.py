import elib

def _primes_in_shell(n):
    corners = [((2 * n + 1) ** 2) - 2 * k * n for k in range(1, 4)]
    return [x for x in corners if elib.is_prime(x)]

def _find_length(target_ratio):
    n = 1
    n_cells = 1
    n_primes = 0

    while True:
        n_cells += 4
        n_primes += len(_primes_in_shell(n))
        if n_primes / n_cells < target_ratio: return 2 * n + 1
        n += 1

_N = 1 << 20
_RATIO = 0.10

#this is slow
def p58():
    print(_find_length(_RATIO))