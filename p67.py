import elib

_FILE = "0067_triangle.txt"
_TEST = """3
7 4
2 4 6
8 5 9 3"""

def _parse_input(_str_rows : list):
    triangle = elib.get_triangular_array(len(_str_rows), 0)

    for row, row_str in enumerate(_str_rows):
        for col, item in enumerate(row_str.split()):
            triangle[row][col] = int(item)

    return triangle

def _get_test_triangle():
    return _parse_input(_TEST.split("\n"))

def _get_triangle():
    _strs = open(_FILE).readlines()
    return _parse_input(_strs)

def _find_path(triangle, paths, row, col):
    if row < col or row >= len(triangle) or col < 0: return 0
    if row == len(triangle) - 1: return triangle[row][col]
    if paths[row][col]: return paths[row][col]

    left = _find_path(triangle, paths, row + 1, col)
    right = _find_path(triangle, paths, row + 1, col + 1)
    paths[row][col] = max(left, right) + triangle[row][col]

    return paths[row][col]

def p67():
    # triangle = _get_test_triangle()
    triangle = _get_triangle()
    paths = elib.get_triangular_array(len(triangle), 0)

    path = _find_path(triangle, paths, 0, 0)
    print(path)
