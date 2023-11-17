import elib

_N = 1_000_000

def _find_palindromes(limit):
    return [x for x in range(limit) 
            if elib.is_palindrome(elib.to_digits(x)) and elib.is_palindrome(elib.to_digits_bin(x))]


def p36():
    print(sum(_find_palindromes(_N)))