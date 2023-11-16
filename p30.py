import elib

_N = 1_000_000

def _sum_digits(number, power):
    return sum (map(lambda x: x ** power, elib.to_digits(number)))

def _find_numbers(limit, power):
    return [x for x in range(2, limit) if x == _sum_digits(x, power)]

def p30():
    print(sum (_find_numbers(_N, 5)))
