from utils import *


inp = get_input(2022, 1)

# part 1
sums = lmap(lambda elf: sum(lmap(int, elf.split("\n"))), inp.split("\n\n"))
print(max(sums))

# part 2
print(sum(sorted(sums)[-3:]))
