import elib

def _sum_of_squares(n):
    return n * (n + 1) * (2 * n + 1) // 6

def _square_of_sum(n):
    x = n * (n + 1) // 2

    return x * x

_N = 100
def p6():
    print(_square_of_sum(_N) - _sum_of_squares(_N))