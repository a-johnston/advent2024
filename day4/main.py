from itertools import permutations

from adventlib import grid, vector

def walk(rows, start, target='XMAS'):
    count = 0
    for d in grid.all_directions:
        ij = start
        for c in target:
            if grid.get(rows, ij) != c:
                break
            ij = vector.add(ij, d)
        else:
            count += 1
    return count

def spin(rows, ij):
    chars = ''.join(str(grid.get(rows, vector.add(ij, d))) for d in grid.diagonals)
    return chars in {'MSSM', 'SMMS', 'SSMM', 'MMSS'}

def solve_p1(lines):
    return sum(walk(lines, ij) for ij in grid.indexes(lines, 'X'))

def solve_p2(lines):
    return sum(spin(lines, ij) for ij in grid.indexes(lines, 'A'))
