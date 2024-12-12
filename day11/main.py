from functools import cache

from adventlib import parse

@cache
def process(stone):
    if stone == 0:
        return (1,)
    l = len(str(stone))
    if l % 2 == 0:
        b = 10 ** int(l / 2)
        return (stone // b,  stone % b)
    return (stone * 2024,)

@cache
def count(stone, times):
    if times == 0:
        return 1
    return sum(count(substone, times - 1) for substone in process(stone))

parse = parse.flat_map(int)
solve_p1 = parse(lambda stones: sum(count(stone, 25) for stone in stones))
solve_p2 = parse(lambda stones: sum(count(stone, 75) for stone in stones))
