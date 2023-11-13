import elib

_t_small = """3
7 4
2 4 6
8 5 9 3"""

_t_big = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

def _parse_row(_str: str) -> list:
    return [int(x) for x in _str.split()]

def _parse_triangle(_str: str) -> list:
    triangle = []

    for s in _str.split("\n"):
        triangle.append(_parse_row(s))

    return triangle

class Triangle:
    def __init__ (self, cells: list):
        self.cells = cells
        self.paths = elib.get_triangular_array(len(cells), 0)

    def _last_row(self, row):
        return row == len(self.cells) - 1
    
    def _last_col(self, col):
        return col == len(self.cells) - 1
    
    def _oob(self, col):
        return col >= len(self.cells)

    def find_path(self, row, col):
        if self.paths[row][col]: return self.paths[row][col]
        if self._last_row(row): return self.cells[row][col]
        if self._oob(col): return 0

        left = self.find_path(row + 1, col)
        right = self.find_path(row + 1, col + 1)
        current = self.cells[row][col] + max(left, right)
        self.paths[row][col] = current

        return current
    
def p18():
    cells = _parse_triangle(_t_big)
    triangle = Triangle(cells)
    print(triangle.find_path(0, 0))

    
    

