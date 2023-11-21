import elib

def _count_powers_for_base(base):
    power = 1
    count = 0

    while True:
        result = base ** power
        if elib.count_digits(result) == power: count += 1
        else: return count
        power += 1

def p63():
    print(sum([_count_powers_for_base(base) for base in range(1, 11)]))