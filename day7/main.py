def possible(total, values, concat=False):
    possible = [0]
    for value in values:
        m = 10 ** len(str(value))
        new = [x * value for x in possible]
        new += [x + value for x in possible]
        if concat:
            new += [x * m + value for x in possible]
        possible = new
    return total in possible

def parse(lines):
    equations = []
    for line in lines:
        a, b = line.split(': ')
        total = int(a)
        values = tuple(map(int, b.split()))
        equations.append((total, values))
    return equations

def helper(lines, concat):
    equations = parse(lines)
    return sum(equation[0] for equation in equations if possible(*equation, concat))

solve_p1 = lambda lines: helper(lines, False)

solve_p2 = lambda lines: helper(lines, True)
