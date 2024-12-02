from collections import Counter

def parse(lines):
    return map(list, zip(*(map(int, filter(None, line.split(' '))) for line in lines)))

def solve_p1(lines):
    a, b = parse(lines)
    a.sort()
    b.sort()
    return sum(map(lambda ab: abs(ab[0] - ab[1]), zip(a, b)))

def solve_p2(lines):
    a, b = map(Counter, parse(lines))
    return sum(map(lambda x: x * a[x] * b[x], a))
