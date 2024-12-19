from functools import cache
from itertools import groupby

def parse(lines):
    it = iter(lines)
    patterns = sorted(next(it).split(', '), key=len)
    patterns = {k: set(v) for k, v in groupby(patterns, len)}
    return patterns, list(filter(None, it))

def get_possible_checker(patterns, get_all):
    @cache
    def check(design):
        total = 0
        if not design:
            return True
        for i in range(1, min(len(design), len(patterns)) + 1):
            if design[:i] in patterns[i]:
                sub = check(design[i:])
                if sub and not get_all:
                    return 1
                total += sub
        return total
    return check

def helper(lines, get_all):
    patterns, designs = parse(lines)
    return sum(map(get_possible_checker(patterns, get_all), designs))

def solve_p1(lines):
    return helper(lines, False)

def solve_p2(lines):
    return helper(lines, True)
