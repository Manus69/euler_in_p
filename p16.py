import elib

def _sum_digits(n: int) -> int:
    _str = str(n)
    _sum = 0

    for k, x in enumerate(_str):
        _sum += int(x)

    return _sum

def p16():
    x = 2 ** 1000
    print(_sum_digits(x))