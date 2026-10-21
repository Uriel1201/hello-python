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

~/hello-python> uv run introcs/birthday.py 365 100000
1, 0, 0.0
2, 234, 0.00234
3, 521, 0.00755
4, 809, 0.01564
5, 1099, 0.02663
6, 1289, 0.03952
7, 1464, 0.05416
8, 1849, 0.07264999999999999
9, 2024, 0.09289
10, 2257, 0.11546000000000001
11, 2497, 0.14043
12, 2589, 0.16632
13, 2832, 0.19464
14, 2930, 0.22394
15, 3005, 0.25399
16, 3102, 0.28501
17, 3155, 0.31656
18, 3202, 0.34858
19, 3268, 0.38126
20, 3199, 0.41325
21, 3274, 0.44599
22, 3248, 0.47847
23, 3152, 0.50999
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
    p = s / trials
    f = np.cumsum(p[1:n + 2])   
    k = np.searchsorted(f, 0.5)               
    stop = min(k + 1, len(f))                
    for i in range(1, stop + 1):
        print(f"{i}, {s[i]}, {f[i - 1]}")

if __name__ == "__main__":
    main()
