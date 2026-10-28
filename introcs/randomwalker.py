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

# Write a program introcs/randomwalker.py that takes an integer command-line argument r
# and simulates the motion of a random walk until the random walker is at Manhattan distance r
# from the starting point.
# Print the coordinates at each step of the walk (including the starting and ending points),
# treating the starting point as (0, 0).
# Also, print the total number of steps taken.

# ~/hello-python> uv run --script introcs/randomwalker.py 5

import argparse
import numpy as np
from numba import njit
import sys
import pyarrow as pa

@njit(cache=True)
def randomwalk(manhattan: int):
    i = j = 0
    steps = [(0, 0)]
    while abs(i) + abs(j) < manhattan:
        x = np.random.random()
        if x < 0.25: i+=1
        elif x < 0.5: i -= 1
        elif x < 0.75: j += 1
        else: j -= 1
        steps.append((i, j))
    return steps

def main() -> None:
    parser    = argparse.ArgumentParser()
    parser.add_argument("manhattan", type=int)
    manhattan = parser.parse_args().manhattan
    if manhattan < 0:
        parser.error("expected a non-negative integer")
    steps     = randomwalk(manhattan)
    X, Y      = map(list, zip(*steps))
    batch = pa.record_batch(
        [pa.array(X), pa.array(Y)],
        names=["X", "Y"],
    )
    with pa.ipc.new_stream(sys.stdout.buffer, batch.schema) as writer:
        writer.write_batch(batch)

if __name__ == "__main__":
    main()
