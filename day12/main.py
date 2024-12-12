from collections import Counter
from dataclasses import dataclass

from adventlib import grid, vector

side_checks = (
    (grid.north, grid.west),
    (grid.south, grid.west),
    (grid.west, grid.north),
    (grid.east, grid.north),
)

@dataclass
class Group:
    index: int
    members: set

    @property
    def area(self):
        return len(self.members)

    @property
    def border(self):
        total = 0
        for member in self.members:
            for d in grid.cardinals:
                if vector.add(member, d) not in self.members:
                    total += 1
        return total

    @property
    def sides(self):
        total = 0
        for member in self.members:
            for a, b in side_checks:
                if (vector.add(member, a) not in self.members
                    and (vector.add(member, b) not in self.members
                         or vector.add(member, b, a) in self.members)):
                    total += 1
        return total

    def merge(self, groups, other):
        self.members |= other.members
        for index in groups:
            if groups[index] == other:
                groups[index] = self

    def __hash__(self):
        return self.index

def search(rows):
    groups = {}
    pos_to_group = {}
    edge = {(0, 0)}
    while edge:
        head = edge.pop()
        this = grid.get(rows, head)
        near_groups = set()
        for d in grid.cardinals:
            other_pos = vector.add(head, d)
            other = grid.get(rows, other_pos)
            if this == other and other_pos in pos_to_group:
                near_groups.add(groups[pos_to_group[other_pos]])
            if other and other_pos not in pos_to_group:
                edge.add(other_pos)
        group = None
        if near_groups:
            group_iter = iter(near_groups)
            group = next(group_iter)
            for other in group_iter:
                group.merge(groups, other)
        else:
            group = Group(len(groups), set())
            groups[group.index] = group
        pos_to_group[head] = group.index
        group.members.add(head)
    return set(groups.values())

def solve_p1(lines):
    groups = search(lines)
    return sum(group.area * group.border for group in groups)

def solve_p2(lines):
    groups = search(lines)
    return sum(group.area * group.sides for group in groups)
