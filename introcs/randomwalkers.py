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

Write a program introcs/randomwalkers.py that takes two integer command-line arguments r and trials.
In each of trials independent experiments, simulate a random walk
until the random walker is at Manhattan distance r from the starting point.
Print the average number of steps.

~/hello-python> uv run --script introcs/randomwalkers 15 20
59
71
49
241
79
83
179
201
165
67
69
103
47
271
405
39
85
67
27
59
Average Steps: 118.3
"""
import argparse
import numpy as np
from numba import njit, prange

@njit(parallel=True, cache=True)
def randomwalks(manhattan: int, trials: int):
    result = np.empty(trials, dtype=np.int64)
    for t in prange(trials):
        i = j = 0
        steps = 0
        while abs(i) + abs(j) < manhattan:
            x = np.random.random()
            if x < 0.25: i+=1
            elif x < 0.5: i -= 1
            elif x < 0.75: j += 1
            else: j -= 1
            steps += 1
        result[t] = steps
    return result 
 
def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("manhattan", type=int)
    parser.add_argument("trials", type=int)
    args = parser.parse_args()
    if args.manhattan < 0:
        parser.error("manhattan must be non-negative")
    if args.trials <= 0:
        parser.error("trials must be positive")
    dist = randomwalks(args.manhattan, args.trials)
    for d in dist:
        print(d)
    average = np.sum(dist) / args.trials
    print(f"Average Steps: {average}")

if __name__ == "__main__":
    main()
