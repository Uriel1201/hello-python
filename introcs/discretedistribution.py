# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "numpy>=2.5.4",
#     "pyarrow>=26.0.0",
# ]
# ///

# Name: Dante1201 (Carlos Uriel García)
# Id:   1201

# Write a program introcs/discretedistribution.py that takes an integer command-line
# argument m, followed by a sequence of positive integer command-line arguments a1,a2,…,an
# and prints m random indices choosing each index i with probability proportional to ai.

# ~/hello-python $ uv run introcs/discretedistribution.py 20 100 200 50 90 120 300 90

import argparse
import sys
import numpy   as np
import pyarrow as pa

def disdist(size: int, lengths: np.ndarray) -> np.ndarray:
    rng = np.random.default_rng()
    s   = np.concatenate(([0], np.cumsum(lengths)))
    p   = rng.integers(0, s[-1], size=size) + 1
    return np.searchsorted(s, p, side="left")

def main() -> None:
    parser        = argparse.ArgumentParser()
    parser.add_argument("size", type=int)
    parser.add_argument("lengths", type=int, nargs="+")
    args          = parser.parse_args()
    size, lengths = args.size, args.lengths
    if size <= 0:
        raise ValueError("Error: size must be positive")
    sample        = disdist(size, np.array(lengths))
    batch         = pa.record_batch([pa.array(sample)], names=["lengths_sample"])
    with pa.ipc.new_stream(sys.stdout.buffer, batch.schema) as writer:
        writer.write_batch(batch)

if __name__ == "__main__":
    main()
