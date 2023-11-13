import math

NO_IDX = -1

def _cast_out(vals: list, n: int):
    step = n
    n += step

    while (n < len(vals)):
        vals[n] = False
        n += step

def _next_prime_idx(vals: list, n: int) -> int:
    n += 1

    while (n < len(vals)):
        if (vals[n]): return n
        n += 1
    
    return NO_IDX

def _sieve_init(vals: list):
    vals[0] = False
    vals[1] = False
    p = 2

    while (True):
        _cast_out(vals, p)
        p = _next_prime_idx(vals, p)
        if (p == NO_IDX): break

_SIEVE_MIN_SIZE = 3
def _sieve_new(size):
    if (size < _SIEVE_MIN_SIZE): size = _SIEVE_MIN_SIZE

    vals = [True] * size
    _sieve_init(vals)

    return vals

def _size_from_prime_count(count: int) -> int:
    return count * 25

class Sieve:
    def __init__ (self, size):
        self.vals = _sieve_new(size)
    
    def resize(self, size):
        self.vals = _sieve_new(size)

    def get_all_primes(self):
        primes = []
        for idx in range(len(self.vals)):
            if (self.vals[idx]): primes.append(idx)
        
        return primes
    
    def is_prime(self, n):
        if (n >= len(self.vals)): self.resize(n + 1)

        return self.vals[n]
    
    def get_n_primes(self, n):
        size = _size_from_prime_count(n)
        if (size >= len(self.vals)): self.resize(size + 1)

        primes = []
        k = 0

        while (len(primes) < n):
            if (self.is_prime(k)): primes.append(k)
            k += 1

        return primes


def get_prime_factors(n: int):
    factors = []
    p = 2

    while (n >= p):
        while (n % p == 0):
            factors.append(p)
            n //= p

        p += 1
    
    return factors

def get_prime_factors_sieve(n: int, sieve: Sieve) -> list:
    if (sieve.is_prime(n)): return [n]

    primes = []
    for k in range(n):
        if sieve.is_prime(k): primes.append(k)

    return primes

def is_palindrome(s: str):
    if (len(s) == 0): return True

    left, right = 0, len(s) - 1
    while (left < right):
        if (s[left] != s[right]): return False
        left += 1
        right -= 1

    return True

def gcd(* args) -> int:
    return math.gcd(* args)

def lcm(* args) -> int:
    return math.lcm(* args)

def pythagorean_triplet_gen(max_side) -> (int, int, int):
    m, n = 2, 1

    while (m < max_side):
        n = 1
        while (n < m):
            yield (m * m - n * n, 2 * m * n, m * m + n * n)
            n += 1
        m += 1

class Table:
    def __init__(self, vals: list, rows, cols):
        self.vals = vals
        self.rows = rows
        self.cols = cols
    
    def get(self, row, col):
        return self.vals[row * self.cols + col]
    
    def n_rows(self):
        return self.rows
    
    def n_cols(self):
        return self.cols

    def __str__(self) -> str:
        _str = []
        for row in range(self.rows):
            for col in range(self.cols):
                _str.append(str(self.get(row, col)))
                _str.append(" ")
            _str.append("\n")
            
        return "".join(_str)