import itertools
import re
from collections import deque

from utils import *


inp = get_input(2022, 5)
inp1, inp2 = inp.split("\n\n")


# lol
parse_stacks = compose(
    lambda m: lzip(*m),  # transpose
    lambda m: lmap(lreversed, m),  # flip horizontal
    lambda m: list(itertools.compress(m, [0, 1, 0, 0] * 9)),  # value rows
    lambda m: lmap(lambda r: lfilter(lambda c: c.strip(), r), m),  # strip ' '
    lambda m: lmap(lambda r: {int(r[0]): r[1:]}, m),  # to lookup table
    lambda dicts: {k: v for d in dicts for k, v in d.items()},  # merge dicts
)


stacks = parse_stacks(inp1.split("\n"))


def parse_move(row):
    pattern = r"move (\d{1,2}) from (\d) to (\d)"
    return lmap(int, re.search(pattern, row).groups())


def tops(d):
    return [v[-1] for _, v in d.items()]


# part 1


def crane1(stacks, moves):
    s = {k: deque(v) for k, v in stacks.items()}
    for move in moves:
        n, fr, to = parse_move(move)
        for i in range(n):
            x = s[fr].pop()
            s[to].append(x)
    return s


print("".join(tops(crane1(stacks, inp2.split("\n")))))


# part 2


def crane2(stacks, moves):
    for move in moves:
        n, fr, to = parse_move(move)
        x = stacks[fr][-n:]
        stacks[fr] = stacks[fr][: -n or None]  # consider copy.deepcopy
        stacks[to].extend(x)
    return stacks


print("".join(tops(crane2(stacks, inp2.split("\n")))))
