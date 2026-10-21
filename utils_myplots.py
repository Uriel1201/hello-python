# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "matplotlib>=3.11.2",
#     "seaborn>=0.13.2",
# ]
# ///
from IPython.display import Image, display
import matplotlib.pyplot as plt
import seaborn as sns

def plot_dist(index_array: np.ndarray) -> None:
    plt.figure(figsize = (9, 7))
    sns.set_theme(style= 'darkgrid')
    plt.title(f'Frequencies')
    plt.ylabel(f'Frequency')
    plt.xlabel(f'index')
    sns.countplot(x = index_array, color = '#088F8F')
    plt.tight_layout()
    plt.savefig("images/discret_distribution.png", dpi=150, bbox_inches="tight")
    plt.close()
    display(Image('images/discret_distribution.png'))
