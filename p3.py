import elib

_n = 600851475143
    

def p3():
    factors = elib.get_prime_factors(_n)
    print(factors[-1])
