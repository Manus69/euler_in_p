import elib

_N = 1_000_000
_chains = [0] * _N

def _next(n: int) -> int:
    if n % 2 == 0: return n // 2

    return 3 * n + 1

def _compute_chain(n: int) -> int:
    if n == 1: return 0
    if n >= _N: return 1 + _compute_chain(_next(n))
    if _chains[n]: return _chains[n]

    chain = 1 + _compute_chain(_next(n))
    _chains[n] = chain

    return chain

def p14():
    max_chain = 0
    idx = 0

    for n in range(1, _N):
        chain = _compute_chain(n)
        if chain > max_chain:
            max_chain = chain
            idx = n

    print(idx)