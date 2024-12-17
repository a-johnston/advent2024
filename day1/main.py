from collections import Counter

from adventlib import parse

@parse.split.map(int).columns(sorted)
def solve_p1(a, b):
    return sum(map(lambda ab: abs(ab[0] - ab[1]), zip(a, b)))

@parse.split.map(int).columns(Counter)
def solve_p2(a, b):
    return sum(map(lambda x: x * a[x] * b[x], a))
