import elib

def _p5(n):
    nums = list(range(1, n + 1))
    return elib.lcm(* nums)

def p5():
    print(_p5(20))