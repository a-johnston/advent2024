import re

matcher = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')

def sum_pairs(matched):
    return sum(map(lambda x: int(x[0]) * int(x[1]), matched))

def solve_p1(lines):
    string = ''.join(lines)
    matched = matcher.findall(string)
    return sum_pairs(matched)

def solve_p2(lines):
    string = ''.join(lines)
    dos = string.split('do()')
    total = 0

    for do in dos:
        matched = matcher.findall(do.split("don't()")[0])
        total += sum_pairs(matched)

    return total
