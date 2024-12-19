import heapq

from adventlib import grid, vector

def parse(lines):
    max_val = 2 ** 32 - 1
    it = iter(lines)
    size, limit = map(int, next(it).split(','))
    rows = [[max_val for _ in range(size)] for __ in range(size)]
    corrupted = []
    for idx, line in enumerate(it, 1):
        x, y = map(int, line.split(','))
        rows[y][x] = idx
        corrupted.append(line)
    return rows, limit, corrupted

def shortest_path(rows, limit):
    start = (0, 0)
    end = len(rows) - 1, len(rows) - 1
    edge = [(0, start)]
    seen = set()
    while edge:
        score, pos = heapq.heappop(edge)
        if pos == end:
            return score
        if pos in seen:
            continue
        seen.add(pos)
        new_score = score + 1
        for d in grid.cardinals:
            new_pos = vector.add(pos, d)
            value = grid.get(rows, new_pos)
            if value is not None and value > limit and new_pos not in seen:
                heapq.heappush(edge, (new_score, new_pos))
    return None

def solve_p1(lines):
    rows, limit, _ = parse(lines)
    return shortest_path(rows, limit)

def solve_p2(lines):
    rows, limit, corrupted = parse(lines)
    lo = limit
    hi = len(corrupted) + 1
    while lo + 1 < hi:
        mid = (hi + lo) // 2
        if shortest_path(rows, mid) is None:
            hi = mid
        else:
            lo = mid
    return corrupted[hi - 1]
