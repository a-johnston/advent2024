from collections import Counter

from adventlib import vector, util

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
    return vector.posmod(vector.add(robot[0], vector.mul(robot[1], steps)), size)

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
    return util.geosum(c.values())

def has_peaks(values):
    values = Counter(values).most_common(2)
    return values[0][1] >= 15 and values[1][1] >= 15

def solve_p2(lines):
    size, robots = parse(lines)
    if size[0] < 50:
        return 'n/a'
    steps, x_peak, y_peak = 0, 0, 0
    while not x_peak or not y_peak:
        steps += 1
        robots = [(sim_steps(size, robot, 1), robot[1]) for robot in robots]
        posmap = {robot[0] for robot in robots}
        if not x_peak and has_peaks((xy[0] for xy in posmap)):
            x_peak = steps
        if not y_peak and has_peaks((xy[1] for xy in posmap)):
            y_peak = steps
    for i in range(max(size)):
        steps = x_peak + size[0] * i
        if (steps - y_peak) % size[1] == 0:
            return steps
