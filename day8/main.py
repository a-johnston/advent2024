from collections import defaultdict
from math import gcd

def valid(limit, i, j):
    return i >= 0 and j >= 0 and i < limit[0] and j < limit[1]

def parse(lines):
    antennas = defaultdict(list)
    limit = len(lines[0]), len(lines)
    for j, line in enumerate(lines):
        for i, c in enumerate(line):
            if c == '.':
                continue
            antennas[c].append((i, j))
    return limit, antennas

def gen_antinodes(antennas):
    for kind, places in antennas.items():
        for a in places:
            for b in places:
                if b <= a:
                    continue
                yield b, (b[0] - a[0], b[1] - a[1])

def solve_p1(lines):
    limit, antennas = parse(lines)
    possible = set()
    for (x, y), (dx, dy) in gen_antinodes(antennas):
        nx, ny = x + dx, y + dy
        if valid(limit, nx, ny):
            possible.add((nx, ny))
        nx, ny = x - 2 * dx, y - 2 * dy
        if valid(limit, nx, ny):
            possible.add((nx, ny))
    return len(possible)

def solve_p2(lines):
    limit, antennas = parse(lines)

    possible = set()
    for (x, y), (dx, dy) in gen_antinodes(antennas):
        n = max(dx, dy) if dx == 0 or dy == 0 else gcd(dx, dy)
        dx, dy = int(dx / n), int(dy / n)
        nx, ny = x, y
        while valid(limit, nx, ny):
            possible.add((nx, ny))
            nx += dx
            ny += dy
        nx, ny = x - dx, y - dy
        while valid(limit, nx, ny):
            possible.add((nx, ny))
            nx -= dx
            ny -= dy
    return len(possible)
