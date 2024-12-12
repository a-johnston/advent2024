import operator
import re

from adventlib import parse, util

matcher = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')

def sum_pairs(matched):
    return sum(util.starmap(operator.mul, util.deep_cast(int, matched)))

@parse.full_text()
def solve_p1(text):
    return sum_pairs(matcher.findall(text))

@parse.full_text()
def solve_p2(text):
    blocks = (do.split("don't()")[0] for do in text.split('do()'))
    return sum(map(sum_pairs, map(matcher.findall, blocks)))
