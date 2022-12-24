import itertools

from utils import *


inp = get_input(2022, 3)


def prio(item):
    # a-z -> 1..26; A-Z -> 27..
    return ord(item) - 96 if item.islower() else ord(item) - (65 - 27)


def common(seq):
    return list(set(seq[0]).intersection(*seq))[0]


# part 1


def halve(sack):
    return sack[: len(sack) // 2], sack[len(sack) // 2 :]


f1 = compose(halve, common, prio)
print(sum(map(f1, inp.split("\n"))))


# part 2


def ungroup(group):
    # extract group vals and remove enumerate
    return lmap(lambda t: t[1], group[1])


grouper = itertools.groupby(enumerate(inp.split("\n")), lambda t: t[0] // 3)
f2 = compose(ungroup, common, prio)
print(sum(map(f2, grouper)))
