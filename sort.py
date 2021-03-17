# investigates how long argsort loops can be
# argsort loops is formed when argsort(argsort(...(a)))... = a
# i.e. repeated application of argsort of an array gets back to the array itself.

from itertools import permutations as P
# from numpy import array as ary
from pprint import pprint
from numpy import argsort

for array_length in range(15):
    sorted_version = {pa:argsort(pa) for pa in P(range(array_length))}

    loop_size = {}
    for key, sorted_key in sorted_version.items():
        traversed_keys = (key,)
        while tuple(sorted_key) not in traversed_keys:
            traversed_keys += (key,)
            key, sorted_key = tuple(sorted_key), sorted_version[tuple(sorted_key)]

        loop_size[key] = len(traversed_keys)

    if array_length<7:
        pprint(loop_size)
    input(f"Completd array size of {array_length}. Conclusion: max loop size = {max(loop_size.values())}")
