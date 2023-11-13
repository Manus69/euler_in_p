import elib
import math

def _sum_digits(n: int) -> int:
    _sum = 0
    for k, x in enumerate(str(n)):
        _sum += int(x)
    
    return _sum

_N = 100
def p20():
    print(_sum_digits(math.factorial(_N)))