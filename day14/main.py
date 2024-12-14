from collections import Counter
from functools import reduce
from operator import mul

from adventlib import vector

def parse(lines):
    it = iter(lines)
    w, h = map(int, next(it).split())
    robots = []
    for line in it:
        l, r = line.split()
        xy = tuple(map(int, l.split('=')[1].split(',')))
        dxy = tuple(map(int, r.split('=')[1].split(',')))
        robots.append((xy, dxy))
    return (w, h), robots

def sim_steps(size, robot, steps):
    xy, dxy = robot
    for _ in range(steps):
        xy = vector.posmod(vector.add(xy, dxy), size)
    return xy

def quad(size, xy):
    x = xy[0] / (size[0] - 1)
    y = xy[1] / (size[1] - 1)
    if x == 0.5 or y == 0.5:
        return None
    return round(x), round(y)

def solve_p1(lines):
    size, robots = parse(lines)
    c = Counter(quad(size, sim_steps(size, robot, 100)) for robot in robots)
    c.pop(None, None)
    return reduce(mul, c.values())

def solve_p2(lines):
    size, robots = parse(lines)
    if size[0] < 50:
        return 'n/a'
    i, j = (size[0] - 1) // 2, (size[1] - 1) // 2
    check = {(ii, jj) for ii in range(i - 1, i + 2) for jj in range(j - 1, j + 2)}
    steps = 0
    while True:
        steps += 1
        robots = [(sim_steps(size, robot, 1), robot[1]) for robot in robots]
        posmap = {robot[0] for robot in robots}
        if check <= posmap:
            return steps
