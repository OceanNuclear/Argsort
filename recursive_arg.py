# investigates how long argsort loops can be
# argsort loops is formed when argsort(argsort(...(a)))... = a
# i.e. repeated application of argsort of an array gets back to the array itself.

from itertools import permutations as P
from numpy import array as ary
from pprint import pprint
from collections import defaultdict
from numpy import argsort

def is1loop(b):
    b = ary(b)
    indices = list(range(len(b)))
    return (b[b] == indices).all()

def is2loop(b):
    return not is1loop(b)

if __name__=="__main__":
    for array_length in range(10):
        sorted_version = {pa:argsort(pa) for pa in P(range(array_length))}
        for key, sorted_key in sorted_version.items():
            if key==tuple(sorted_key):
                print(key)
                print(tuple(sorted_key))
                print("")

        loop_size = {}
        loop_size_count = defaultdict(int)
        for key, sorted_key in sorted_version.items():
            traversed_keys = (key,)
            # while tuple(sorted_key) not in traversed_keys:
            while tuple(sorted_key) != traversed_keys[0]:
                traversed_keys += (key,)
                key, sorted_key = tuple(sorted_key), sorted_version[tuple(sorted_key)]

            loop_size[key] = len(traversed_keys)
            if loop_size[key]==1:
                assert is1loop(sorted_key), "My is1loop gives false negatives."
            else:
                assert not is1loop(sorted_key), "my is1loop checker gives False positives."

        for loop_length in loop_size.values():
            loop_size_count[loop_length] += 1
        # if array_length<7:
        #     pprint(loop_size)

        print(f"Loop size counts = {loop_size_count}")
        print("The fraction of self-loops = {}".format(loop_size_count[1]/sum(loop_size_count.values())))
        input(f"Completd array size of {array_length}. Conclusion: max loop size = {max(loop_size.values())}\n")
