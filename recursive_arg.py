"""
Proved on paper: argsort(argsort(a))==a.
But we want to find out under what condition does argsort(a)==a.
____
Well! Turns out this sequence of numbers that my program prints out is related to this:
https://oeis.org/A000085
And what I once called 1loop are actually technically named involutions.
"""
from itertools import permutations as P
import numpy as np
from numpy import array as ary

def deterministic(n=1):
    """Analytically run through all permutations of np.arange(n) to check if they're cycle length = 2 vectors or not."""
    while n:
        num_perms, non_self_argsort = 0, 0
        for pa in P(range(n)):
            num_perms += 1
            if (np.argsort(pa)!=ary(pa)).any():
                non_self_argsort += 1
            else:
                print(pa)
        input(f"For vectors of size n={n}, {num_perms-non_self_argsort}/{num_perms} has a cycle length = 1")
        n += 1

def probabilistic(n=1, num_samples=100000):
    """Randomly sample whether a specific permutation gives a cycle length = 2 vectors or not."""
    while n:
        non_self_argsort = 0
        a0 = np.arange(n)
        a1 = a0
        for _ in range(num_samples):
            init_a = a1.copy()
            np.random.shuffle(a1)
            non_self_argsort += int((a1!=init_a).any())
        input(f"For vectors of size n={n}, {non_self_argsort}/{num_samples} has a cycle length = 2")
        n += 1

if __name__=="__main__":
    deterministic()
    # np.random.seed(0)
    # probabilistic()