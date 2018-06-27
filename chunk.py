"""
Break a list into smaller chunks for processing. 
"""

import math
import random


def chunk(lst, chunk_size=10):
    """
    Return a generator which will yield chunks of lst. Each chunk will have
    `chunk_size` elements in it (the last chunk may be shorter).
    """

    if chunk_size < 1:
        raise ValueError('chunk_size must be at least 1')

    l = len(lst)
    i = 0
    while i < l:
        yield lst[i:i+chunk_size]
        i += chunk_size


def chunk_grow(lst, chunk_size=10, growth=2):
    """
    Return a generator which will yield chunks of lst. Each chunk will be of
    increasing size, using `growth` as the growth factor (the last chunk may
    be shorter).
    """

    if chunk_size < 1:
        raise ValueError('chunk_size must be at least 1')

    l = len(lst)
    i = 0
    while i < l:
        yield lst[i:i+chunk_size]
        i += chunk_size
        chunk_size = math.floor(chunk_size * growth)


def chunk_rand(lst, min_chunk_size=2, max_chunk_size=10):
    """
    Return a generator which will yield chunks of lst. Each chunk will be or
    random size within `min_chunk_size` and `max_chunk_size` (the last chunk
    may be shorter than `min_chunk_size`).
    """

    if min_chunk_size < 1:
        raise ValueError('min)_chunk_size must be at least 1')
    
    if min_chunk_size > max_chunk_size:
        raise ValueError('min_chunk_size must be less than max_chunk_size')
    
    l = len(lst)
    i = 0
    
    while i < l:
        chunk_size = random.randint(min_chunk_size, max_chunk_size)
        yield lst[i:i+chunk_size]
        i += chunk_size


def main():
    lst = list(range(73))
    for c in chunk(lst):
        print(c)
    
    for c in chunk_grow(lst, 2, 1.5):
        print(c)

    for c in chunk_rand(lst, 2, 5):
        print(c)

if __name__ == '__main__':
    main()