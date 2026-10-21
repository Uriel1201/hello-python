# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "numpy>=2.5.4",
# ]
# ///
"""
Name: Dante1201 (Carlos Uriel García)
Id:   1201

Write a program introcs/discretedistribution.py that takes an integer command-line
argument m, followed by a sequence of positive integer command-line arguments a1,a2,…,an
and prints m random indices choosing each index i with probability proportional to ai.

~/hello-python> uv run introcs/discretedistribution.py 20 100 200 50 90 120 300 90
6
2
6
4
6
4
1
2
5
4
7
6
6
6
6
2
1
4
2
5
"""
import argparse
import numpy as np

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("args", type=int, nargs="+")
    params = parser.parse_args().args
    if len(params) < 2:
        parser.error("Usage: m a1 a2 ... an")
    m = params.pop(0)
    values = np.array(params, dtype=np.int64)
    if m <= 0 or (values <= 0).any():
        parser.error("m and all a_i must be positive")
    s = np.concatenate(([0], np.cumsum(values)))
    p = np.random.randint(0, s[-1], size=m) 
    sample = np.searchsorted(s, p, side="right")
    for value in sample:
        print(value)

if __name__ == "__main__":
    main()
