import os
from pathlib import Path

import requests
from dotenv import load_dotenv


load_dotenv()


def get_input(year, day):
    inp = _get_cached_input(year, day)
    if inp:
        print(f"Found cached input for {year} day {day}.")
        return inp.rstrip()

    print(f"Fetching input for {year} day {day}... ", end="")
    res = requests.get(
        f"https://adventofcode.com/{year}/day/{day}/input",
        headers=dict(cookie=f'session={os.getenv("SESSION")}'),
    )
    res.raise_for_status()

    print("Done.")
    _cache_input(year, day, res.text)
    return res.text.rstrip()


def _get_cached_input(year, day):
    p = Path(f"data/{year}_{day:02}.txt")
    return p.read_text() if p.exists() else None


def _cache_input(year, day, inp):
    print(f"Caching input for {year} day {day}... ", end="")
    p = Path(f"data/{year}_{day:02}.txt")
    p.parent.mkdir(exist_ok=True)
    p.write_text(inp)
    print("Done.")


def lmap(f, it):
    return list(map(f, it))


def lfilter(f, it):
    return list(filter(f, it))


def lzip(*it):
    return list(zip(*it))


def lreversed(it):
    return list(reversed(it))


def dinvert(d):
    return dict(map(reversed, d.items()))


def compose(*fs):
    def inner(arg):
        for f in fs:
            arg = f(arg)
        return arg

    return inner


def printdict(d):
    for k, v in d.items():
        print(f"{k}: {v}")
