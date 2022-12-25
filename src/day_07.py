import collections
import pathlib
import re

from utils import *


inp = get_input(2022, 7)


def fqfn(d, f):
    return str(pathlib.PurePath(d, f))


def graph(log):
    children, files = collections.defaultdict(set), dict()
    parent, pwd = dict(), ""

    for line in log:
        if match := re.search(r"^\$ cd (.+)$", line):
            if (new := match.group(1)) != "..":
                parent[fqfn(pwd, new)] = pwd
                pwd = fqfn(pwd, new)
            else:
                pwd = parent[pwd]
        elif line == "$ ls":
            continue
        else:
            size, name = line.split(" ")
            children[pwd].add(fqfn(pwd, name))
            if size.isnumeric():
                files[fqfn(pwd, name)] = int(size)

    return children, files


def dirsizes(root, children, files):
    totals = dict()

    def traverse(root):
        total = 0
        for c in children[root]:
            total += files[c] if c in files else traverse(c)
        totals[root] = total
        return total

    traverse(root)
    return totals


# part 1
totals = dirsizes("/", *graph(inp.split("\n")))
print(sum(lfilter(lambda size: size < 100_000, totals.values())))

# part 2
free = 70_000_000 - totals["/"]
print(min(lfilter(lambda v: (v + free) > 30_000_000, totals.values())))
