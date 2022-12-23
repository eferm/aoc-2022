import os
from pathlib import Path

import requests
from dotenv import load_dotenv


load_dotenv()


def get_input(year, day):
    inp = _get_cached_input(year, day)
    if inp:
        print(f"Found cached input for {year} day {day}.")
        return inp.strip()

    print(f"Fetching input for {year} day {day}... ", end="")
    res = requests.get(
        f"https://adventofcode.com/{year}/day/{day}/input",
        headers=dict(cookie=f'session={os.getenv("SESSION")}'),
    )
    res.raise_for_status()

    print("Done.")
    _cache_input(year, day, res.text)
    return res.text.strip()


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


def dinvert(d):
    return dict(map(reversed, d.items()))
