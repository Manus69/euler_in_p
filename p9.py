import elib

def _p9(max_side):
    p_gen = elib.pythagorean_triplet_gen(max_side)

    while (True):
        t = next(p_gen, None)
        if t is None: break
        if ((t[0] + t[1] + t[2]) == max_side): return t[0] * t[1] * t[2]

    return 0

def p9():
    print(_p9(1000))