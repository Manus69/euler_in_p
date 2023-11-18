import elib

def _get_number_string(limit):
    return ''.join([str(x) for x in range(limit)])

def _product(_str):
    return int(_str[1]) * int(_str[10]) * int(_str[100]) * int(_str[1000]) * int(_str[10_000]) \
            * int(_str[100_000]) * int(_str[1_000_000])

_N = 1_000_000
def p40():
    print(_product(_get_number_string(_N)))