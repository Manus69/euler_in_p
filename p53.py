import elib

_MAX = 1_000_000

def _compute_nck(nck_dict : dict, n, k):
    if k == 0: return 1
    if k == n: return 1

    left = nck_dict[(n - 1, k - 1)]
    right = nck_dict[(n - 1, k)]

    return left + right

def _compute_all_ncks(n_max):
    nck_dict = {}
    nck_dict[(0, 0)] = 1

    for n in range(n_max + 1):
        for k in range(n + 1):
            nck = _compute_nck(nck_dict, n, k)
            nck_dict[(n, k)] = nck

    return nck_dict

def p53():
    nck_dict = _compute_all_ncks(100)
    print(sum([1 for x in nck_dict.values() if x > _MAX]))