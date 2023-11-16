import elib

def _find_unique(base_max, power_max) -> set:
    return set([b ** p for b in range(2, base_max + 1) for p in range(2, power_max + 1)])

_A = 100
_B = 100

def p29():
    print(len(_find_unique(_A, _B)))