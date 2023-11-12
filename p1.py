def _sum(n):
    sum = 0
    for k in range(n):
        if ((k % 3 == 0) or (k % 5 == 0)): sum += k
    
    return sum

def p1():
    print(_sum(1000))
    