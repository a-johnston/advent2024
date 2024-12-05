from collections import defaultdict

def parse(lines):
    reqs = defaultdict(set)
    updates = []

    for line in lines:
        if '|' in line:
            a, b = line.split('|')
            reqs[int(b)].add(int(a))
        if ',' in line:
            updates.append(tuple(map(int, line.split(','))))
    return reqs, updates

def correct(update, reqs):
    involved = set(update)
    have = set()
    for page in update:
        if (reqs[page] & involved) - have:
            return False
        have.add(page)
    return True

def fix(update, reqs):
    fixed = []
    have = set()
    involved = set(update)
    to_fix = set(update)
    while to_fix:
        for page in to_fix:
            if not ((reqs[page] & involved) - have):
                have.add(page)
                fixed.append(page)
                to_fix.remove(page)
                break
    return fixed

def mid(update):
    return update[int(len(update) / 2)]

def solve_p1(lines):
    reqs, updates = parse(lines)
    return sum(mid(update)
               for update in updates
               if correct(update, reqs))

def solve_p2(lines):
    reqs, updates = parse(lines)
    return sum(mid(fix(update, reqs))
               for update in updates
               if not correct(update, reqs))
