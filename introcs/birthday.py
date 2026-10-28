# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "numba>=0.68.0",
#     "numpy>=2.5.4",
#     "pyarrow>=26.0.0",
# ]
# ///

# Name: Dante1201 (Carlos Uriel García)
# Id:   1201

# Write a program introcs/birthday.py that takes two integer command-line arguments n
# and trials and performs the following experiment, trials times:

# - Choose a birthday for the next person, uniformly at random between 0 and n−1.
# - Have that person enter the room.
# - If that person shares a birthday with someone else in the room, stop; otherwise repeat.

# In each experiment, count the number of people that enter the room.
# Plot an scatterplot that summarizes the results (the number of times that exactly i people
# enter the room, and the fraction of times that i or fewer people enter the room)
# for each possible value of i from 1 until the fraction reaches (or exceeds) 50%.

# ~/hello-python $ uv run introcs/birthday.py 365 100000

import argparse
import sys
import numpy as np
from numba import njit
import pyarrow as pa

@njit(cache=True)
def birthday_simulation(n: int, trials: int) -> np.ndarray:
    s    = np.zeros(n + 2, dtype=np.int64)
    seen = np.zeros(n, dtype=np.int64)
    for t in range(trials):
        mark  = t + 1
        count = 0
        while True:
            p     = np.random.randint(0, n)
            count += 1
            if seen[p] == mark:
                break
            seen[p] = mark
        s[count] += 1
    return s

def main() -> None:
    parser     = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    parser.add_argument("trials", type=int)
    args       = parser.parse_args()
    n, trials  = args.n, args.trials
    if n <= 0 or trials <= 0:
        raise ValueError("Invalid arguments")
    simulation = birthday_simulation(n, trials)
    f          = np.cumsum(simulation[1:n + 2]) / trials
    k          = np.arange(1, len(simulation) + 1)
    batch = pa.record_batch(
        [pa.array(k), pa.array(simulation), pa.array(f)],
        names=["k", "frequency", "p_k"],
    )
    with pa.ipc.new_stream(sys.stdout.buffer, batch.schema) as writer:
        writer.write_batch(batch)

if __name__ == "__main__":
    main()
