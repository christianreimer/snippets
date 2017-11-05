"""
Using bisect to to create ranges (buckets) of values for the keys in a dict.
"""

import bisect
import collections
import random
import pprint


def main():
    buckets = [1, 2, 3, 5, 8, 13, 21, 34]
    range_func = lambda x: bisect.bisect(buckets, x)
    range_dict = collections.defaultdict(int)

    for _ in range(100):
        range_dict[range_func(random.randint(0, 50))] += 1

    pprint.pprint(dict(range_dict), width=10)


if __name__ == '__main__':
    main()
