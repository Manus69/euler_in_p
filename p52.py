import elib

def _check_number(x):
    if elib.count_digits(x) != elib.count_digits(6 * x): return False

    return set(elib.to_digits(x)) == \
            set(elib.to_digits(2 * x)) == \
            set(elib.to_digits(3 * x)) == \
            set(elib.to_digits(4 * x)) == \
            set(elib.to_digits(5 * x)) == \
            set(elib.to_digits(6 * x))

def _find_number():
    x = 1
    while True:
        if _check_number(x): return x
        x += 1

_N = 125874

def p52():
    print(_find_number())