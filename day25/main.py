def to_int(row):
    total = 0
    for val in row:
        total = total * 16 + val
    return total

def parse(lines):
    keys, locks = [], []
    for entry in '\n'.join(lines).split('\n\n'):
        pivot = list(map(''.join, zip(*entry.split('\n'))))
        val = to_int([len(x.strip('.')) for x in pivot])
        (keys if entry[0] == '#' else locks).append(val)
    return keys, locks

def solve_p1(lines):
    mask = to_int([8, 8, 8, 8, 8])
    keys, locks = parse(lines)
    total = 0
    for key in keys:
        for lock in locks:
            if (key + lock) & mask == 0:
                total += 1
    return total
