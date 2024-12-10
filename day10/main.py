dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))

def valid(grid, i, j):
    return i >= 0 and j >= 0 and j < len(grid) and i < len(grid[j])

def parse(lines):
    grid = [list(map(int, line)) for line in lines]
    starts = []
    for j, row in enumerate(grid):
        for i, x in enumerate(row):
            if grid[j][i] == 0:
                starts.append((i, j))
    return grid, starts

def score(lines, rating):
    grid, starts = parse(lines)
    total = 0
    for idx, start in enumerate(starts):
        edge = [start]
        summits = list() if rating else set()
        while edge:
            i, j = edge.pop()
            if grid[j][i] == 9:
                (summits.append if rating else summits.add)((i, j))
            else:
                for di, dj in dirs:
                    ni, nj = i + di, j + dj
                    if valid(grid, ni, nj) and grid[j][i] + 1 == grid[nj][ni]:
                        edge.append((ni, nj))
        total += len(summits)
    return total

solve_p1 = lambda lines: score(lines, False)

solve_p2 = lambda lines: score(lines, True)
