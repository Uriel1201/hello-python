# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "numpy>=2.5.4",
# ]
# ///
"""
Name: Dante1201 (Carlos Uriel García)
Id:   1201

Write a program introcs/bandmatrix.py that takes two integer
command-line arguments n and width and prints an n-by-n pattern,
with a zero (0) for each element whose distance from the main diagnonal is
strictly more than width, and an asterisk (*) for each entry that is not.
Here, distance means the minimum number of cells you have to move
(either left, right, up, or down) to reach the main diagonal.

~/hello-python> uv run --script introcs/bandmatrix 15 4
* * * * * 0 0 0 0 0 0 0 0 0 0
* * * * * * 0 0 0 0 0 0 0 0 0
* * * * * * * 0 0 0 0 0 0 0 0
* * * * * * * * 0 0 0 0 0 0 0
* * * * * * * * * 0 0 0 0 0 0
0 * * * * * * * * * 0 0 0 0 0
0 0 * * * * * * * * * 0 0 0 0
0 0 0 * * * * * * * * * 0 0 0
0 0 0 0 * * * * * * * * * 0 0
0 0 0 0 0 * * * * * * * * * 0
0 0 0 0 0 0 * * * * * * * * *
0 0 0 0 0 0 0 * * * * * * * *
0 0 0 0 0 0 0 0 * * * * * * *
0 0 0 0 0 0 0 0 0 * * * * * *
0 0 0 0 0 0 0 0 0 0 * * * * *
"""

import argparse
import numpy as np

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("args", type=int, nargs="+")
    params = parser.parse_args().args
    if len(params) < 2:
        parser.error("Usage: n, width")
    n = params.pop(0)
    w = params.pop(0)
    if n < 0 or w < 0:
        parser.error("Error: expected non-negative integers")
    i, j = np.indices((n, n))
    bandmatrix = np.abs(i - j) <= w
    for row in np.where(bandmatrix, "*", "0"):
        print(" ".join(row))

if __name__ == "__main__":
    main()
