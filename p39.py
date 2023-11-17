import elib

def _get_solution_set(limit):
    primitives = [x for x in elib.pythagorean_triplet_gen_max_side(limit)]
    triplets = []

    for triplet in primitives:
        k = 2
        while True:
            current = tuple([x * k for x in triplet])
            if sum(current) > limit: break
            triplets.append(current)
            k += 1
    
    primitives.extend(triplets)
    return primitives

def _count_solutions(triplets, limit):
    counts = {}

    for triplet in triplets:
        p = sum(triplet)
        if p > limit: continue
        if p in counts: counts[p] += 1
        else: counts[p] = 1
    
    return counts

_P = 1000

def p39():
    triplets = _get_solution_set(_P)
    slns = _count_solutions(triplets, _P)
    print(max(slns.keys(), key=slns.get))