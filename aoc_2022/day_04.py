from utils import *


inp = get_input(2022, 4)


def expand(assignment):
    def range1(start, stop):
        return range(start, stop + 1)

    return list(range1(*map(int, assignment.split("-"))))


f = compose(
    lambda r: r.split(","),
    lambda r: lmap(expand, r),
)

# part 1


def compare(pair):
    return set(pair[0]).issubset(pair[1]) or set(pair[1]).issubset(pair[0])


f1 = compose(f, compare)
print(sum(map(f1, inp.split("\n"))))


# part 2


def overlap(pair):
    return bool(set(pair[0]).intersection(pair[1]))


f2 = compose(f, overlap)
print(sum(map(f2, inp.split("\n"))))
