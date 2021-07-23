from recursive_arg import *

if __name__=="__main__":
    for array_length in range(1,10):
        sorted_version = {pa:argsort(pa) for pa in P(range(array_length))}
        same_cd = 0
        for key, sorted_key in sorted_version.items():

            a = ary(key)
            b = a[a]
            c = a[b]
            d = a[b][b]
            similarity = c==d

            same_cd += similarity.all()
        print(f"{same_cd}/{len(sorted_version)} of them has 100% match")
        input(f"End of {array_length=}")