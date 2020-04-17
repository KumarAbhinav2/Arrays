"""function which will take a number k as input and return two numbers that add up to k.
Input- lst = [1,21,3,14,5,60,7,6]
       k = 81
Output - lst = [21,60]
"""
import unittest

# Intuitive way

def add_upto_intuitive(lst, k):
    for i in lst:
        for j in lst:
            if i+j == k and lst.index(i) != lst.index(j):
                return [i, j]


def add_upto_better(lst, k):
    # sort the array
    lst.sort()
    start = 0
    end = len(lst) - 1
    while start < len(lst) and end > start:
        temp_sum = lst[start]+lst[end]
        if temp_sum == k:
            return [lst[start], lst[end]]
        elif temp_sum > k:
            end -= 1
        elif temp_sum < k:
            start +=1
    return None

class TestMergeList(unittest.TestCase):

    def setUp(self) -> None:
        self.list1 = [1,21,3,14,5,60,7,6]
        self.k = 81
        self.actual_output = [21,60]

    def test_add_upto_intuitive(self):
        result = add_upto_intuitive(self.list1, self.k)
        self.assertEqual(result, self.actual_output)

    def test_add_upto_better(self):
        result = add_upto_better(self.list1, self.k)
        self.assertEqual(result, self.actual_output)

