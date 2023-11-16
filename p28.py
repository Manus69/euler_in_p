import elib

def _shell_corner_sum(k):
    if k == 0: return 1

    return 4 * (2 * k + 1) * (2 * k + 1) - 12 * k

def _diag_sum(radius):
    _sum = 0
    for k in range(radius): _sum += _shell_corner_sum(k)

    return _sum

_N = 1001

def p28():
    print(_diag_sum(_N // 2 + 1))