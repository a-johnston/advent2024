from collections import Counter

pos_mon = { 1, 2, 3 }
neg_mon = { -1, -2, -3 }
opts = (pos_mon, neg_mon)

def parse(lines):
    return (list(map(int, line.split())) for line in lines)

def invert(report):
    return (-val for val in report)

def is_safe_helper(it):
    last = next(it)
    for val in it:
        delta = val - last
        if delta < 1 or delta > 3:
            return False
        last = val
    return True

def is_safe(report):
    return any(is_safe_helper(r) for r in (iter(report), invert(report)))

def solve_p1(lines):
    return sum(is_safe(report) for report in parse(lines))

def solve_p2(lines):
    count = 0
    for report in parse(lines):
        for i in range(len(report)):
            new_report = report[:i] + report[i + 1:]
            if is_safe(new_report):
                count += 1
                break
    return count
