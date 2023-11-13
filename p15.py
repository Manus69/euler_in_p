import elib

def _count_routes(row, col, tbl: elib.Table):
    if row == tbl.n_rows(): return 1
    if col == tbl.n_cols(): return 1
    if tbl.get(row, col): return tbl.get(row, col)

    down = _count_routes(row + 1, col, tbl)
    right = _count_routes(row, col + 1, tbl)
    tbl.set(row, col, down + right)

    return tbl.get(row, col)

_N = 20
def p15():
    table = elib.Table([0] * _N * _N, _N, _N)
    print(_count_routes(0, 0, table))