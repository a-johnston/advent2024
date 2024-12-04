from itertools import permutations

walk_dirs = set(permutations((0, 1, 1, -1, -1), 2))
spin_dirs = ((1, 1), (1, -1), (-1, -1), (-1, 1))

def valid(lines, i, j):
    return i >= 0 and j >= 0 and j < len(lines) and i < len(lines[j])

def walk(lines, i, j, target='XMAS'):
    count = 0
    for d in walk_dirs:
        ii, jj = i, j
        for c in target:
            if not valid(lines, ii, jj) or lines[jj][ii] != c:
                break
            ii, jj = ii + d[0], jj + d[1]
        else:
            count += 1
    return count

def spin(lines, i, j):
    if any(not valid(lines, i + d[0], j + d[1]) for d in spin_dirs):
        return False
    chars = ''.join(lines[j + d[1]][i + d[0]] for d in spin_dirs)
    return chars in {'MSSM', 'SMMS', 'SSMM', 'MMSS'}

def indexes(lines, char):
    for j in range(len(lines)):
        yield from ((i, j) for (i, c) in enumerate(lines[j]) if c == char)

def solve_p1(lines):
    return sum(walk(lines, i, j) for (i, j) in indexes(lines, 'X'))

def solve_p2(lines):
    return sum(spin(lines, i, j) for (i, j) in indexes(lines, 'A'))
