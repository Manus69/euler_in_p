import elib

def _letter_to_number(x):
    return ord(x) - ord('A') + 1

def _sum_letters(_str: str):
    _sum = 0
    for k, x in enumerate(_str):
        _sum += _letter_to_number(x)

    return _sum

def _score(lines: list) -> int:
    score = 0
    for k, _str in enumerate(lines):
        score += (k + 1) * _sum_letters(_str)

    return score

_FILE = "0022_names.txt"
def p22():
    file = open(_FILE)
    lines = file.readline().split(",")
    lines = [x.strip("\"") for x in lines]
    lines.sort()
    print(_score(lines))
