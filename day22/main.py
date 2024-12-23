from collections import defaultdict

import numpy as np

m = 16777216

def iter_secret(x):
    x = (x ^ (x << 6)) % m
    x = (x ^ (x >> 5)) % m
    return (x ^ (x << 11)) % m

def solve_p1(lines):
    a = np.array(lines, int)
    for _ in range(2000):
        a = iter_secret(a)
    return int(sum(a))

def solve_p2(lines):
    a = np.array(lines, int)
    options = defaultdict(set)
    totals = defaultdict(int)
    last, deltas = a % 10, np.zeros((len(lines),))
    for i in range(2000):
        a = iter_secret(a)
        prices = a % 10
        deltas = (deltas * 20 + (prices - last) + 10) % (20 ** 4)
        last = prices
        if i > 3:
            for j, values in enumerate(np.column_stack((deltas, prices))):
                key, price = map(int, values)
                if key not in options[j]:
                    options[j].add(key)
                    totals[key] += price
    return max(totals.values())
