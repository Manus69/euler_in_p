import elib

_FILE = "0059_cipher.txt"
_FREQUENT_SYMBOLS = (' ', 'e', 't')
_KEY_LEN = 3

def _get_most_frequent(_list):
    _dict = {}
    for x in _list:
        if x in _dict: _dict[x] += 1
        else: _dict[x] = 1
    
    return max(_dict.keys(), key=_dict.get)

def _get_key(vals):
    frequent_vals = [_get_most_frequent(vals[::3]),
                     _get_most_frequent(vals[1::3]),
                     _get_most_frequent(vals[2::3])]
    frequent_vals = [x ^ ord(_FREQUENT_SYMBOLS[0]) for x in frequent_vals]
    return frequent_vals

def _map_key(vals, key):
    return [vals[k] ^ key[k % _KEY_LEN] for k in range(len(vals))]

def _display_text(vals, key):
    print("".join(map(lambda x : chr(x), _map_key(vals, key))))

def _compute_sum(vals, key):
    return sum(_map_key(vals, key))

def p59():
    text = open(_FILE).read()
    vals = [int(x) for x in text.split(',')]
    key = _get_key(vals)
    # _display_text(vals, key)
    print(_compute_sum(vals, key))
