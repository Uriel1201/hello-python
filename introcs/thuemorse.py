# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "numpy>=2.5.4",
# ]
# ///
"""
Write a program introcs/thuemorse.py that takes 
// an integer command-line argument n and prints an n-by-n pattern. 
// and creates an n-by-n pattern by printing a + (plus sign) in row i
// and column j if bits i and j in the sequence are equal, 
// and a - (minus sign) if they are different.
 
~/hello-python> uv run --script introcs/thuemorse.py 200
"""

import argparse
import numpy as np

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=np.int64)
    n = parser.parse_args().n
    if n < 0:
        parser.error("expected a non-negative integer")
    i, j = np.indices((n, n))
    pairs = np.bitwise_count(i ^ j) % 2
    for row in np.where(pairs==0, "+", "-"):
        print(" ".join(row))

if __name__ == "__main__":
    main()
