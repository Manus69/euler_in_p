import math
from operator import mul
from functools import reduce

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

_SIEVE_DC = 1 << 10
class Sieve:
    def __init__ (self, size = _SIEVE_DC):
        self.vals = _sieve_new(size)
    
    def resize(self, size):
        self.vals = _sieve_new(size)

    def get_primes_lt(self, n):
        if (n >= len(self.vals)): self.resize(n + 1)

        primes = []
        for idx in range(n):
            if (self.is_prime(idx)): primes.append(idx)

        return primes

    def get_all_primes(self):
        return self.get_primes_lt(len(self.vals) - 1)
    
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

def get_divisors(n: int):
    divisors = [1]
    if n == 1: return divisors

    d = 2

    while d * d < n:
        if n % d == 0:
            divisors.append(d)
            divisors.append(n // d)
        
        d += 1

    if d * d == n: divisors.append(d)
    divisors.append(n)

    return divisors

def get_prime_factors_sieve(n: int, sieve: Sieve) -> list:
    if sieve.is_prime(n): return [n]

    primes = sieve.get_primes_lt(n)
    divisors = []

    for p in primes:
        if p > n: break
        while n % p == 0:
            divisors.append(p)
            n //= p

    return divisors

def count_divisors(n: int) -> int:
    p_powers = []
    p = 2

    if n == 1: return 1

    while n >= p:
        if n % p == 0:
            p_powers.append(0)
            while n % p == 0:
                p_powers[-1] += 1
                n //= p
        p += 1
    
    return reduce(mul, [x + 1 for x in p_powers])

def is_palindrome(s):
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

def trianglen_gen() -> int:
    n = 0

    while True:
        yield n * (n + 1) // 2
        n += 1

def get_rect_array(rows, cols, default_val):
    array = []
    for row in range(rows):
        array.append([default_val] * cols)
    
    return array

def get_triangular_array(rows, default_val):
    array = []
    for row in range(rows):
        array.append([default_val] * (1 + row))

    return array

class Table:
    def __init__(self, vals: list, rows, cols):
        self.vals = vals
        self.rows = rows
        self.cols = cols
    
    def get(self, row, col):
        return self.vals[row * self.cols + col]
    
    def set(self, row, col, val):
        self.vals[row * self.cols + col] = val

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

def rev(_list: list, idx, _len):
    _list[idx : idx + _len] = _list[idx + _len - 1 : idx - 1 : -1]

class Permutation:
    def _get_suffix_len(self):
        idx = len(self.vals) - 1
        while idx > 0:
            if self.vals[idx] > self.vals[idx - 1]: break
            idx -= 1
        
        return len(self.vals) - idx
    
    def _find_first_greater(self, suffix_len):
        val = self.vals[len(self.vals) - suffix_len - 1]
        for idx in range(len(self.vals) - 1, 0, -1):
            if self.vals[idx] > val: return idx
        
        raise RuntimeError

    def _swap_rev(self, left, right):
        self.vals[left], self.vals[right] = self.vals[right], self.vals[left]
        rev(self.vals, left + 1, len(self.vals) - left - 1)

    def __init__(self, vals: list):
        self.vals = vals

    def __iter__(self):
        return self
    
    def __next__ (self):
        suffix_len = self._get_suffix_len()
        if suffix_len == len(self.vals): raise StopIteration
        
        left = len(self.vals) - suffix_len - 1
        right = self._find_first_greater(suffix_len)
        self._swap_rev(left, right)

def fib_gen() -> int:
    f0, f1 = 0, 1
    while True:
        yield f0
        f0, f1 = f1, f0 + f1

def count_digits(x: int) -> int:
    return math.log10(x or 1) + 1

def to_digits(x : int , base = 10):
    digits = []
    while True:
        digits.append(x % base)
        x //= base
        if x == 0: break

    digits.reverse()
    return digits

def to_digits_bin(x : int):
    return to_digits(x, 2)