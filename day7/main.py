from itertools import islice

def possible(values, concat=False):
    total, possible = values[0], [values[1]]
    for value in islice(values, 2, len(values) - 1):
        m = 10 ** len(str(value))
        new = []
        for x in possible:
            if x > total:
                continue
            new.append(x * value)
            new.append(x + value)
            if concat:
                new.append(x * m + value)
        possible = new
    value = values[-1]
    m = 10 ** len(str(value))
    for x in possible:
        if x + value == total:
            return True
        if x * value == total:
            return True
        if concat and x * m + value == total:
            return True
    return False

def parse(lines):
    return (tuple(map(int, line.replace(':', '').split())) for line in lines)

def helper(lines, concat):
    return sum(vals[0] for vals in parse(lines) if possible(vals, concat))

solve_p1 = lambda lines: helper(lines, False)

solve_p2 = lambda lines: helper(lines, True)
