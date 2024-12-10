from collections import namedtuple

Grid = namedtuple('Grid', ('limit', 'obstacles', 'hitcache'))

dirs = ((0, -1), (1, 0), (0, 1), (-1, 0))

def add(a, b):
    return tuple(map(sum, zip(a, b)))

def valid(grid, i, j):
    return i >= 0 and j >= 0 and i < grid.limit[0] and j < grid.limit[1]

def scan(grid, ij, d):
    cached = grid.hitcache.get((*ij, d))
    if cached:
        return cached
    visited = set()
    update = []
    subpath = set()
    hit = None
    while valid(grid, *ij):
        key = (*ij, d)
        if key in grid.hitcache:
            # Use cached subpath and result if available
            hit, subpath = grid.hitcache[key]
            visited |= subpath
            break
        # Otherwise, mark the key to be cached when the scan finishes
        update.append(key)
        visited.add(ij)
        ij = add(ij, dirs[d])
        if ij in grid.obstacles:
            hit = ij
            break
    # In reverse order, update cache keys to maintain subpath invariant
    while update:
        key = update.pop()
        i, j, _ = key
        subpath = {(i, j)} | subpath
        grid.hitcache[key] = hit, subpath
    return hit, visited

def walk(grid, pos, check=None):
    d = 0
    turns = set()
    hit, visited = scan(grid, pos, d)
    if check in visited:
        hit = check
    turns.add((hit, d))
    while hit:
        pos = add(hit, dirs[(d + 2) % len(dirs)])
        d = (d + 1) % len(dirs)
        hit, path = scan(grid, pos, d)
        if check in path:
            hit = check
        if (hit, d) in turns:
            return True, visited
        turns.add((hit, d))
        if not check:
            visited |= path
    return False, visited

def parse(lines):
    grid = Grid((len(lines[0]), len(lines)), set(), dict())
    pos = None
    for j, line in enumerate(lines):
        if '^' in line:
            pos = line.index('^'), j
        for i, c in enumerate(line):
            if c == '#':
                grid.obstacles.add((i, j))
    return grid, pos

def solve_p1(lines):
    grid, pos = parse(lines)
    return len(walk(grid, pos)[1])

def solve_p2(lines):
    grid, pos = parse(lines)
    return sum(walk(grid, pos, step)[0]
               for step in walk(grid, pos)[1]
               if step != pos)
