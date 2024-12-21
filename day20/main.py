import heapq

from adventlib import grid 

key_factor = 150

key_deltas = (1, -1, key_factor, -key_factor)

def key(xy):
    return xy[1] * key_factor + xy[0]

def parse(lines):
    print(len(lines[0]), len(lines))
    start = next(map(key, grid.indexes(lines, 'S')))
    end = next(map(key, grid.indexes(lines, 'E')))
    spots = set(map(key, grid.indexes(lines, '.')))
    spots.add(start)
    spots.add(end)
    return spots, end

def bfs(pos, is_valid_child):
    edge, distances = [(0, pos)], {pos: 0}
    while edge:
        dist, pos = heapq.heappop(edge)
        new_dist = dist + 1
        for delta in key_deltas:
            new_pos = pos + delta
            if new_pos not in distances and is_valid_child(new_pos, dist):
                distances[new_pos] = new_dist
                heapq.heappush(edge, (new_dist, new_pos))
    return distances

def get_dists(spots, end):
    return bfs(end, lambda pos, dist: pos in spots)

def get_conv(distance):
    return bfs(0, lambda pos, dist: dist < distance)

def get_cheats(distances, conv, report_limit=100):
    for pos, dist in distances.items():
        for offset, offset_dist in conv.items():
            new_pos = pos + offset
            if new_pos in distances:
                skipped = dist - distances[new_pos] - offset_dist
                if skipped >= report_limit:
                    yield 1

def helper(lines, cheat_distance):
    return sum(get_cheats(get_dists(*parse(lines)), get_conv(cheat_distance)))

solve_p1 = lambda lines: helper(lines, 2)
solve_p2 = lambda lines: helper(lines, 20)
