"""
Utility functions to make it easy to work with bitmaps.
"""

def set(bitmap, bit):
    bitmap |= 1 << bit
    return bitmap

def clear(bitmap, bit):
    bitmap &= ~(1 << bit)
    return bitmap

def flip(bitmap, bit):
    bitmap ^= 1 << bit
    return bitmap

def test(bitmap, bit):
    return (bitmap & (1 << bit)) > 0

def empty(bitmap):
    return bitmap == 0

def display(bitmap):
    return bin(bitmap)

def union(bitmap1, bitmap2):
    return bitmap1 | bitmap2

def intersect(bitmap1, bitmap2):
    return bitmap1 & bitmap2
