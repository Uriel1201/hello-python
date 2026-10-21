# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "numba>=0.68.0",
#     "numpy>=2.5.4",
# ]
# ///
"""
Name: Dante1201 (Carlos Uriel García)
Id:   1201

Write a program introcs/birthday.py that takes two integer command-line arguments n
and trials and performs the following experiment, trials times:

- Choose a birthday for the next person, uniformly at random between 0 and n−1.
- Have that person enter the room.
- If that person shares a birthday with someone else in the room, stop; otherwise repeat.

In each experiment, count the number of people that enter the room.
Plot an scatterplot that summarizes the results (the number of times that exactly i people 
enter the room, and the fraction of times that i or fewer people enter the room)
for each possible value of i from 1 until the fraction reaches (or exceeds) 50%.

~/hello-python> env -u MPLBACKEND uv run introcs/birthday.py 365 100000
"""
import argparse
import numpy as np
from numba import njit

@njit(cache=True)
def simulate_birthday(n: int, trials: int) -> np.ndarray:
    s = np.zeros(n + 2, dtype=np.int64)
    seen = np.zeros(n, dtype=np.int64) 
    for t in range(trials):
        mark = t + 1
        count = 0
        while True: 
            p = np.random.randint(0, n)
            count += 1
            if seen[p] == mark:
                break
            seen[p] = mark
        s[count] += 1
    return s

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    parser.add_argument("trials", type=int)
    args = parser.parse_args()
    n, trials = args.n, args.trials
    if n <= 0 or trials <= 0:
        raise ValueError("Invalid arguments")
    s = simulate_birthday(n, trials)
    f = 0.0
    for i in range(1, n + 2):
        f += s[i] / trials
        print(f"{i}, {s[i]}, {f}")
        if f >= 0.5:
            break

if __name__ == "__main__":
    main()
