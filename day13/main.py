from itertools import count

from adventlib import vector

def parse_x_y(line):
    xs, ys = line.split(': ')[1].split(', ')
    return int(xs[2:]), int(ys[2:])

def parse(lines):
    it = iter(lines)
    for a in it:
        if not a:
            continue
        yield parse_x_y(a), parse_x_y(next(it)), parse_x_y(next(it))

def tokens(a, b, c, limit=float('inf'), bonus=0):
    det = a[0] * b[1] - a[1] * b[0]
    if det != 0:
        c = vector.add(c, (bonus, bonus))
        i = (b[1] * c[0] - b[0] * c[1]) / det
        j = (a[0] * c[1] - a[1] * c[0]) / det
        if all(x == int(x) and x < limit for x in (i, j)):
            return int(i) * 3 + int(j)
    return 0

def solve_p1(lines):
    return sum(tokens(*vals, limit=100) for vals in parse(lines))

def solve_p2(lines):
    return sum(tokens(*vals, bonus=10 ** 13) for vals in parse(lines))
