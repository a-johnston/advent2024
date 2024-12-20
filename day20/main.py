from collections import defaultdict
import heapq

from adventlib import grid, vector

def parse(lines):
    start = next(grid.indexes(lines, 'S'))
    end = next(grid.indexes(lines, 'E'))
    spots = set(grid.indexes(lines, '.'))
    spots.add(start)
    spots.add(end)
    return start, end, spots

def aa_bfs(pos, is_valid_child):
    edge, distances = [(0, pos)], {pos: 0}
    while edge:
        dist, pos = heapq.heappop(edge)
        new_dist = dist + 1
        for direction in grid.cardinals:
            new_pos = vector.add(pos, direction)
            if new_pos not in distances and is_valid_child(new_pos, dist):
                distances[new_pos] = new_dist
                heapq.heappush(edge, (new_dist, new_pos))
    return distances

def get_distance_map(spots, end):
    return aa_bfs(end, lambda pos, dist: pos in spots)

def get_cheat_convolution(distance):
    return aa_bfs((0, 0), lambda pos, dist: dist < distance)

def get_cheats(distances, conv):
    skips = defaultdict(set)
    for pos, dist in distances.items():
        for offset, offset_dist in conv.items():
            new_pos = vector.add(pos, offset)
            new_dist = distances.get(new_pos)
            if new_dist is not None:
                skipped = dist - new_dist - offset_dist
                if skipped > 0:
                    skips[skipped].add((pos, new_pos))
    return skips

def helper(lines, cheat_distance):
    start, end, spots = parse(lines)
    skips = get_cheats(
        get_distance_map(spots, end),
        get_cheat_convolution(cheat_distance),
    )
    return sum(len(v) for k, v in skips.items() if k >= 100)

solve_p1 = lambda lines: helper(lines, 2)
solve_p2 = lambda lines: helper(lines, 20)
