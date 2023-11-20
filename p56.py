import elib

def _digit_sum(x : int) -> int:
    return sum(elib.to_digits(x))

_N = 100

def p56():
    numbers = [a ** b for a in range(_N) for b in range(_N)]
    print(sum(elib.to_digits(max(numbers, key=_digit_sum))))
    