import elib

def _is_palindrome(n: int):
    return elib.is_palindrome(str(n))

def _p4(low, high):
    current = 0
    _max = 0

    for k in range(low, high):
        for w in range(k, high):
            current = k * w
            if (_is_palindrome(current) and current > _max): _max = current
    
    return _max

def p4():
    print(_p4(100, 1000))