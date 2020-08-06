# TODO: Hangyu Lin (John), hl2357
# TODO: Guanchen Zhang (James), gz256

# Please see instructions.pdf for the description of this problem.
from fixed_size_array import FixedSizeArray
from cs5112_hash import cs5112_hash1
from cs5112_hash import cs5112_hash2
from cs5112_hash import cs5112_hash3

# Implementation of a basic bloom filter. Uses exactly three hash functions.
class BloomFilter:
    def __init__(self, size=10):
        # DO NOT EDIT THIS CONSTRUCTOR
        self.size = size
        self.array = FixedSizeArray(size)
        for i in range(0, size):
            self.array.set(i, False)

    # To add an element to the bloom filter, use each of the k=3 hash functions we provided and compute
    # the positions that we are setting in the fixed size array using modulo operation.
    def add_elem(self, elem):
        hash1 = cs5112_hash1(elem)%10
        hash2 = cs5112_hash2(elem)%10
        hash3 = cs5112_hash3(elem)%10
        self.array.set(hash1, True)
        self.array.set(hash2, True)
        self.array.set(hash3, True)

    # Returns False if the given element was definitely not added to the filter. 
    # Returns True if it's possible that the element was added to the filter.
    def check_membership(self, elem):
        hash1 = cs5112_hash1(elem)%10
        hash2 = cs5112_hash2(elem)%10
        hash3 = cs5112_hash3(elem)%10
        if self.array.get(hash1) and self.array.get(hash2) and self.array.get(hash3):
            return True
        else:
            return False