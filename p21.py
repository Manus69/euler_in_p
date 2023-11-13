import elib

_N = 10_000

def _compute_div_sums(div_sum_tbl: list, sieve: elib.Sieve):
    for k in range(len(div_sum_tbl)):
        divisors = elib.get_divisors(k)
        divisors.pop()
        div_sum_tbl[k] = sum(divisors)

def _get_amicable(div_sum_tbl: list):
    numbers = []
    for k in range(2, len(div_sum_tbl)):
        val = div_sum_tbl[k]
        if val == k: continue
        if val >= len(div_sum_tbl): continue
        if div_sum_tbl[val] == k: numbers.append(k)
    
    return numbers

def p21():
    div_sum_table = [0] * _N
    sieve = elib.Sieve(_N)
    _compute_div_sums(div_sum_table, sieve)
    print(sum(_get_amicable(div_sum_table)))