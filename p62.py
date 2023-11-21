import elib

def _get_cubes(limit):
    return [x ** 3 for x in range(limit)]

def _get_digits(cubes):
    return [sorted(elib.to_digits(x)) for x in cubes]

def _get_permutations(idx, digits):
    return [k ** 3 for k in range(len(digits)) if digits[k] == digits[idx]]

def _find_n_perms(digits, n):
    for k in range(len(digits)):
        if len(_get_permutations(k, digits)) == n: return k ** 3
    
    return 0

_N = 10_000

def p62():
    cubes = _get_cubes(_N)
    digits = _get_digits(cubes)
    print(_find_n_perms(digits, 5))