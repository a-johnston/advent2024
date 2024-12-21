from functools import cache

from adventlib import vector

A = 'A'

class Pad:
    def __init__(self, pad):
        self.pad = pad
        self.inv = {v: k for k, v in pad.items()}

    @cache
    def nav(self, start, end):
        start_pos, end_pos = self.pad[start], self.pad[end]
        dx = end_pos[0] - start_pos[0]
        dy = end_pos[1] - start_pos[1]
        x_moves = ('>' if dx > 0 else '<') * abs(dx)
        y_moves = ('v' if dy > 0 else '^') * abs(dy)
        x_first = x_moves + y_moves + A
        y_first = y_moves + x_moves + A
        if vector.add(start_pos, (dx, 0)) not in self.inv:
            return y_first
        if vector.add(start_pos, (0, dy)) not in self.inv:
            return x_first
        return y_first if dx > 0 else x_first

    def get_moves(self, sequence):
        for a, b in zip(A + sequence, sequence):
            yield self.nav(a, b)

keypad = Pad({'0': (-1, 0), '1': (-2, -1), '2': (-1, -1), '3': (0, -1),
              '4': (-2, -2), '5': (-1, -2), '6': (0, -2), '7': (-2, -3),
              '8': (-1, -3), '9': (0, -3), A: (0, 0)})

dpad = Pad({'^': (-1, 0), '<': (-2, 1), 'v': (-1, 1), '>': (0, 1), A: (0, 0)})

@cache
def dpad_stack(sequence, left):
    if left < 1:
        return len(sequence)
    return sum(dpad_stack(move, left - 1) for move in dpad.get_moves(sequence))

def helper(lines, dpads):
    total = 0
    for line in lines:
        mult = int(line.lstrip('0').rstrip('A'))
        subtotal = 0
        for move in keypad.get_moves(line):
            subtotal += dpad_stack(move, dpads)
        total += subtotal * mult
    return total

def solve_p1(lines):
    return helper(lines, 2)

def solve_p2(lines):
    return helper(lines, 25)
