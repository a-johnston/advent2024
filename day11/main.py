from functools import cache

def parse(lines):
    yield from map(int, ' '.join(lines).split())

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

solve_p1 = lambda lines: sum(count(stone, 25) for stone in parse(lines))

solve_p2 = lambda lines: sum(count(stone, 75) for stone in parse(lines))
