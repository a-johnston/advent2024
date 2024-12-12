from collections import Counter

from adventlib import grid, vector

side_checks = (
    (grid.north, grid.west),
    (grid.south, grid.west),
    (grid.west, grid.north),
    (grid.east, grid.north),
)

def border(group):
    total = 0
    for member in group:
        for d in grid.cardinals:
            if vector.add(member, d) not in group:
                total += 1
    return total

def sides(group):
    total = 0
    for member in group:
        for a, b in side_checks:
            if (vector.add(member, a) not in group
                and (vector.add(member, b) not in group
                     or vector.add(member, b, a) in group)):
                total += 1
    return total

def search(rows):
    seen = set()
    group = set()
    edge = set()
    prio = {(0, 0)}
    while prio or edge:
        if not prio and group:
            yield group
            group = set()
        head = (prio or edge).pop()
        if head in seen:
            continue
        group.add(head)
        seen.add(head)
        val = grid.get(rows, head)
        for cardinal in grid.cardinals:
            other_pos = vector.add(head, cardinal)
            other = grid.get(rows, other_pos)
            if not other or other_pos in seen:
                continue
            (prio if val == other else edge).add(other_pos)
    if group:
        yield group

def solve_p1(lines):
    return sum(len(group) * border(group) for group in search(lines))

def solve_p2(lines):
    return sum(len(group) * sides(group) for group in search(lines))
