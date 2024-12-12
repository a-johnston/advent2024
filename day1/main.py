from collections import Counter

from adventlib import parse

@parse.column_map(int, sorted)
def solve_p1(a, b):
    return sum(map(lambda ab: abs(ab[0] - ab[1]), zip(a, b)))

@parse.column_map(int, Counter)
def solve_p2(a, b):
    return sum(map(lambda x: x * a[x] * b[x], a))
