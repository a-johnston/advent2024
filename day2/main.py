from collections import Counter

from adventlib import parse, vector

def is_safe_helper(it):
    last = next(it)
    for val in it:
        delta = val - last
        if delta < 1 or delta > 3:
            return False
        last = val
    return True

def is_safe(report):
    return any(map(is_safe_helper, (iter(report), iter(vector.invert(report)))))

@parse.row_map(int)
def solve_p1(reports):
    return sum(map(is_safe, reports))

@parse.row_map(int)
def solve_p2(reports):
    count = 0
    for report in reports:
        for i in range(len(report)):
            new_report = report[:i] + report[i + 1:]
            if is_safe(new_report):
                count += 1
                break
    return count
