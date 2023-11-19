import elib
import functools

_FILE = "0042_words.txt"

def _get_items(_file):
    return [x.strip("\"") for x in open(_file).read().split(",")]

def _max_len(_strings):
    return len(max(_strings, key=len))

def _max_possible_score(_strings):
    return _max_len(_strings) * ord("Z")

def _score(_str):
    return sum([ord(x) - ord("A") + 1 for x in _str])

def _get_tr_set(limit):
    vals = []
    f = elib.trianglen_gen()
    while True:
        current = next(f)
        if current > limit: break
        vals.append(current)
    
    return set(vals)


def p42():
    items = _get_items(_FILE)
    max_score = _max_possible_score(items)
    tr_set = _get_tr_set(max_score)
    scores = [_score(_str) for _str in items]
    print(sum([1 for s in scores if s in tr_set]))