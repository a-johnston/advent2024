from collections import namedtuple
import heapq

from adventlib import hint, grid, util, vector
from adventlib.hint import first

State = namedtuple('State', ('score', 'pos', 'facing', 'path'))

def turn(facing, delta):
    return util.posmod(facing + delta, len(grid.cardinals))

def get_adjacent(places, place):
    return {vector.add(place, card)
            for card in grid.cardinals
            if vector.add(place, card) in places}

def parse(lines):
    size, start, end, places = grid.get_data(lines, first('S'), first('E'), '.')
    places.add(start)
    places.add(end)
    return size, start, end, places

def solve_p1(lines):
    _, start, end, places = parse(lines)

    # (score, pos, dir)
    visited = {}
    edge = [(0, start, 0)]
    while edge:
        score, pos, facing = heapq.heappop(edge)
        visited[(pos, facing)] = score
        if pos == end:
            return score
        options = [(score + 1, vector.add(pos, grid.cardinals[facing]), facing)]
        for delta in (-1, 1):
            new = turn(facing, delta)
            options.append((score + 1001, vector.add(pos, grid.cardinals[new]), new))
        for option in options:
            if option[1] in places:
                key = (option[1], option[2])
                if key not in visited or visited[key] > score:
                    heapq.heappush(edge, option)

def solve_p2(lines):
    size, start, end, places = parse(lines)

    visited = {}
    best = None
    reached_by = set()
    edge = [(0, start, 0, {start})]
    while edge:
        score, pos, facing, path = heapq.heappop(edge)
        visited[(pos, facing)] = score
        if pos == end:
            if best is None or score < best:
                reached_by = set()
                best = score
            if score > best:
                break
            reached_by |= path

        options = [(score + 1, vector.add(pos, grid.cardinals[facing]), facing)]
        for delta in (-1, 1):
            new = turn(facing, delta)
            options.append((score + 1001, vector.add(pos, grid.cardinals[new]), new))
        for option in options:
            if option[1] in places:
                option = [*option, {*path, option[1]}]
                key = (option[1], option[2])
                if key not in visited or visited[key] > score:
                    heapq.heappush(edge, option)
    return len(reached_by)
