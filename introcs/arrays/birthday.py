# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "matplotlib>=3.11.2",
#     "numba>=0.68.0",
#     "numpy>=2.5.4",
#     "seaborn>=0.13.2",
# ]
# ///
"""
Name: Dante1201 (Carlos Uriel García)
Id:   1201

Write a program introcs/arrays/birthday.py that takes two integer command-line arguments n
and trials and performs the following experiment, trials times:

- Choose a birthday for the next person, uniformly at random between 0 and n−1.
- Have that person enter the room.
- If that person shares a birthday with someone else in the room, stop; otherwise repeat.

In each experiment, count the number of people that enter the room.
Print a table that summarizes the results (the count i, the number of times that
exactly i people enter the room, and the fraction of times that i or fewer people enter the room)
for each possible value of i from 1 until the fraction reaches (or exceeds) 50%.

~/hello-python> !env -u MPLBACKEND uv run introcs/arrays/birthday.py 365 100000
1, 0, 0.000000
2, 2720, 0.002720
3, 5581, 0.008301
4, 8146, 0.016447
5, 10733, 0.027180
6, 13316, 0.040496
7, 15884, 0.056380
8, 18068, 0.074448
9, 20083, 0.094531
10, 22346, 0.116877
11, 24189, 0.141066
12, 25699, 0.166765
13, 27474, 0.194239
14, 28796, 0.223035
15, 29805, 0.252840
16, 30440, 0.283280
17, 31266, 0.314546
18, 32170, 0.346716
19, 32278, 0.378994
20, 32064, 0.411058
21, 32470, 0.443528
22, 32019, 0.475547
23, 31574, 0.507121
"""

import argparse
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from numba import njit

@njit(cache=True)
def simulate(n: int, trials: int) -> np.ndarray:
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

def plot_birthday(frequencies:np.array) -> None:
    index = np.arange(1, len(frequencies) + 1)
    plt.figure(figsize = (7, 9))
    sns.set(style = 'darkgrid')
    plt.title(f'P_X(x) = 0.50')
    plt.xlabel(f'x')
    plt.ylabel(f'Cumulative')
    sns.scatterplot(x = index, y = frequencies, color = '#088F8F')
    f_x = index[-1]
    f_y = frequencies[-1]
    plt.text(x = f_x, y = f_y, s = f'{f_x}', color = '#8f0808', ha = 'right', va = 'baseline')
    plt.axhline(y = 0.5, color = '#8f0808', linestyle = ':')
    plt.tight_layout()
    plt.savefig("images/birthday.png", dpi=150, bbox_inches="tight")
    plt.close()

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    parser.add_argument("trials", type=int)
    args = parser.parse_args()
    n, trials = args.n, args.trials
    if n <= 0 or trials <= 0:
        raise ValueError("Invalid arguments")
    s = simulate(n, trials)
    f = 0.0
    list = []
    for i in range(1, n + 2):
        f += s[i] / trials
        list.append(f)
        print(f"{i}, {s[i]}, {f}")
        if f >= 0.5:
            break
    frequencies = np.array(list)
    plot_birthday(frequencies)

if __name__ == "__main__":
    main()
