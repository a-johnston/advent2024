from itertools import count

from adventlib import vector

def parse_x_y(line):
    xs, ys = line.split(': ')[1].split(', ')
    return int(xs[2:]), int(ys[2:])

def parse(lines, bonus=0):
    it = iter(lines)
    for a in it:
        if not a:
            continue
        a = parse_x_y(a)
        b = parse_x_y(next(it))
        target = vector.add(parse_x_y(next(it)), (bonus, bonus))
        yield a, b, target

def tokens(a, b, c, limit=None):
    x1, y1 = a
    x2, y2 = b
    det = x1 * y2 - y1 * x2
    if det == 0:
        return 0
    x3, y3 = c
    i = (y2 * x3 - x2 * y3) / det
    j = (x1 * y3 - y1 * x3) / det
    if i == int(i) and j == int(j):
        return int(i) * 3 + int(j)
    return 0

def solve_p1(lines):
    return sum(tokens(*vals, 100) for vals in parse(lines))

def solve_p2(lines):
    return sum(tokens(*vals) for vals in parse(lines, 10000000000000))
