
def _fib():
    x0, x1 = 0, 1
    while (True):
        yield x0
        x0, x1 = x1, x0 + x1

def _sum(limit: int) -> int:
    f = _fib()
    sum = 0

    while True:
        x = next(f)
        if (x > limit): break
        sum += (x % 2 == 0) * x
    
    return sum

def p2():
    print(_sum(4_000_000))
    