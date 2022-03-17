"""
Investigates what happens when you repeatedly apply the sort index
Are argsort sequences unique?
    Yes, because inverse exists.
Turns out this sequence has the name:
    Landau's Function G(n)
https://oeis.org/A000793
"""
import json
from pprint import pprint
from itertools import permutations as P
import numpy as np
from numpy import array as ary
from collections import defaultdict
import matplotlib.pyplot as plt

def brute_force(n=1):
    """Brute force computation to count loop sizes over all permutations of np.arange(n)"""
    while n:
        loop_size_counter = defaultdict(int)
        sorted_array = np.arange(n)
        for pa in P(range(n)):
            pa = ary(pa)
            new_array = sorted_array.copy()[pa]
            num_applications = 1
            while not (new_array==sorted_array).all():
                new_array = new_array[pa]
                num_applications += 1
            loop_size_counter[num_applications] += 1
            if num_applications==1:
                print(pa, "has loop size = 1")
        print(f"At {n=}, loop sizes=")
        pprint(dict(loop_size_counter), width=1)
        input()
        n += 1

def brute_force_argsort(n=1):
    """Same as brute_force, but more convoluted.
    turns out it just runs through all permutations as well, because argsort is a bijective function."""
    raise DeprecationWarning
    while n:
        loop_size_counter = defaultdict(int)
        sorted_array = np.arange(n)
        for pa in P(range(n)):
            pa = ary(pa)
            indexer = np.argsort(pa)
            new_array = sorted_array.copy()
            num_applications = 2
            while not (new_array==pa).all():
                new_array = new_array[indexer]
                num_applications += 1
            loop_size_counter[num_applications] += 1
        print(f"At {n=}, loop sizes=")
        pprint(dict(loop_size_counter), width=1)
        input()
        n += 1

def histogram(json_file):

    """Plot a histogram using the data printed that is saved to the json file."""
    with open(json_file) as j:
        hist_data = json.load(j)
    for n, data in hist_data.items():
        loop_sizes, counts = zip(*[(int(k), int(v)) for k, v in data.items()])
        plt.bar(loop_sizes, counts,)
        plt.title("n="+n)
        plt.xlabel("loop size")
        plt.ylabel("counts")
        plt.xticks(np.arange(1, max([30, max(loop_sizes)])+1))
        if max(loop_sizes)<31:
            plt.xlim([-1, 31])
        plt.show()

if __name__=="__main__":
    # brute_force()
    # brute_force_argsort()
    histogram("repeated_indexing.json")