# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "matplotlib>=3.11.2",
#     "seaborn>=0.13.2",
#     "numpy>=2.5.4",
# ]
# ///
import os
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

os.makedirs("images", exist_ok=True)

def plot_birthday(frequencies:np.array) -> None:
    index = np.arange(1, len(frequencies) + 1)
    plt.figure(figsize = (7, 9))
    sns.set(style = 'darkgrid')
    plt.title(f'P_X(x) = 0.50')
    plt.xlabel(f'x')
    plt.ylabel(f'Cumulative')
    sns.scatterplot(x = index, 
        y = frequencies, 
        color = '#088F8F'
    )
    f_x = index[-1]
    f_y = frequencies[-1]
    plt.text(x = f_x, 
        y = f_y, 
        s = f'{f_x}', 
        color = '#8f0808', 
        ha = 'right',
        va = 'baseline'
    )
    plt.axhline(y = 0.5, 
        color = '#8f0808', 
        linestyle = ':'
    )
    plt.tight_layout()
    plt.savefig("images/birthday.png", 
        dpi=150, 
        bbox_inches="tight"
    )
    plt.close()

def main():
