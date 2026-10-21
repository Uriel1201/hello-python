# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "numpy>=2.5.4",
#     "matplotlib>=3.11.2",
#     "seaborn>=0.13.2",
#     "ipython",
# ]
# ///
"""
Name: Dante1201 (Carlos Uriel García)
Id:   1201

Write a program introcs/discretedistribution.py that takes an integer command-line
argument m, followed by a sequence of positive integer command-line arguments a1,a2,…,an
and plots m random indices choosing each index i with probability proportional to ai.

~/hello-python> env -u MPLBACKEND uv run introcs/discretedistribution.py 1000000 100 200 50 90 120 300 90
"""
from utils_myplots import plot_dist
import argparse
import numpy as np

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("args", type=int, nargs="+")
    params = parser.parse_args().args
    if len(params) < 2:
        raise ValueError("Usage: m a1 a2 ... an")
    print("Hello from discretedistribution.py!")
    m = params.pop(0)
    values = np.array(params)
    s = np.concatenate(([0], np.cumsum(values)))
    p = np.random.randint(0, s[-1], size=m) 
    sample = np.searchsorted(s, p, side="right")
    plot_dist(sample)

if __name__ == "__main__":
    main()
