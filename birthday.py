#---------------------------------------------------------
"""
# The Birthday Problem.
## An application to Occupancy Problems
Consider the conceptual 'experiment' of randomly tagging items into n labels. 
The random tagging of items continues until for the first time 
an item is tagged into a label already occupied.

The Birthday Problem amount to this: If we select people at random one by one, 
how many people shall we have to sample in order to find 
a pair with a common birthday?
"""
#---------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


#---------------------------------------------------------
"""
This simulation shows off the amazing result that, 
among 't' number of trials, the fraction in which 
the first duplicate birthday happens before the 24th person enters 
surpasses 50%.
"""

def main():
    n = int(input("The range for the variable X: "))
    trials= int(input("Number of Simulations: "))
    m = n + 2
    s = np.zeros(m, dtype = int)
    for t in range(trials):
        birthday = np.zeros(n, dtype = bool)
        count = 0
        for j in range(n + 1):
            p = int(np.random.rand() * n)
            count += 1
            if birthday[p]:
                break
            birthday[p] = True
        s[count] += 1
    cumulative_frequency = 0.0
    frequency_list = []
    for i in range(1, m):
        cumulative_frequency += (1.0 * s[i] / trials)
        frequency_list.append(cumulative_frequency)
        if cumulative_frequency >= 0.5:
            break
    frequency_array = np.array(frequency_list)
    index = np.arange(1, len(frequency_array) + 1)
    plt.figure(figsize = (7, 9))
    sns.set(style = 'darkgrid')
    plt.title(f'The Moment in which the Fraction Surpassed 0.50')
    plt.xlabel(f'The Size of the Sample')
    plt.ylabel(f'Fraction in Which First Duplicate Happened for Lower Sizes')
    sns.scatterplot(x = index, y = frequency_array, color = '#088F8F')
    f_x = index[-1]
    f_y = frequency_array[-1]
    plt.text(x = f_x, y = f_y, s = f'{f_x}', color = '#8f0808', ha = 'right', va = 'baseline')
    plt.axhline(y = 0.5, color = '#8f0808', linestyle = ':')
    plt.tight_layout()
    plt.show()


#---------------------------------------------------------
if __name__ == '__main__':
    main()
