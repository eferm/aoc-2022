from utils import *


inp = get_input(2022, 2)
rounds = lmap(lambda r: r.split(" "), inp.split("\n"))

winning = {"A": "C", "B": "A", "C": "B"}


def score(opp, me):
    vals = {"A": 1, "B": 2, "C": 3}
    return vals[me] + (6 if winning[me] == opp else 3 if me == opp else 0)


# part 1
norm = {"X": "A", "Y": "B", "Z": "C"}
print(sum(map(lambda r: score(r[0], norm[r[1]]), rounds)))


# part 2
pick = {
    "X": lambda opp: winning[opp],
    "Y": lambda opp: opp,
    "Z": lambda opp: dinvert(winning)[opp],
}
print(sum(map(lambda r: score(r[0], pick[r[1]](r[0])), rounds)))
