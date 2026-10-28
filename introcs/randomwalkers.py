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

# Write a program introcs/randomwalkers.py that takes two integer command-line arguments r and trials.
# In each of trials independent experiments, simulate a random walk
# until the random walker is at Manhattan distance r from the starting point.
# Print the average number of steps.

# ~/hello-python $ uv run --script introcs/randomwalkers.py 15 20

import sys
import argparse
import numpy as np
import pyarrow as pa
from numba import njit, prange

@njit(cache=True)
def randomwalk(manhattan: int) -> int:
    i = j = 0
    steps = 0
    while abs(i) + abs(j) < manhattan:
        x = np.random.random()
        if x < 0.25: i+=1
        elif x < 0.5: i -= 1
        elif x < 0.75: j += 1
        else: j -= 1
        steps += 1
    return steps

@njit(parallel=True, cache=True)
def randomwalks(manhattan: int,
    trials: int
):
    result = np.empty(trials, dtype=np.int64)
    for t in prange(trials):
        result[t] = randomwalk(manhattan)
    return result

def main() -> None:
    parser     = argparse.ArgumentParser()
    parser.add_argument("manhattan", type=int)
    parser.add_argument("trials", type=int)
    args       = parser.parse_args()
    if args.manhattan < 0:
        parser.error("manhattan must be non-negative")
    if args.trials <= 0:
        parser.error("trials must be positive")
    steps = randomwalks(args.manhattan, args.trials)
    means = np.cumsum(steps) / np.arange(1, args.trials + 1)
    
    batch = pa.record_batch(
        [pa.array(steps), pa.array(means)],
        names=["x_i", "(x_1 +...+ x_i)/i"]
    )
    with pa.ipc.new_stream(sys.stdout.buffer, batch.schema) as writer:
        writer.write_batch(batch)
    
if __name__ == "__main__":
    main()
