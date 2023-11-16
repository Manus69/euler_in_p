import elib

_target = 200
_coins = [1, 2, 5, 10, 20, 50, 100, 200]
_ways = elib.get_rect_array(len(_coins) + 1, _target + 1, elib.NO_IDX)

def _count_ways(n_coins, target):
    if target < 0: return 0
    if target == 0: return 1
    if n_coins == 0: return 0
    if _ways[n_coins][target] != elib.NO_IDX: return _ways[n_coins][target]

    use = _count_ways(n_coins, target - _coins[n_coins - 1])
    skip = _count_ways(n_coins - 1, target)

    _ways[n_coins][target] = use + skip
    return use + skip

def p31():
    print(_count_ways(len(_coins), 200))