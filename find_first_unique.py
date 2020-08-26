"""
Implement a function, findFirstUnique(lst) that returns the first unique integer in the list.

Input - arr = [9,2,3,2,6,6]
output - 9
"""

mymap = {}
for i in arr:
    if i in mymap.items():
        del mymap[i]
    else:
        mymap[i] = arr.insert()


























import unittest
import time
from collections import OrderedDict

# Intuitive way

def findFirstUnique_intuitive(lst):
    for i in range(len(lst)):
        j = 0
        while j<len(lst):
            if i!=j and lst[i] == lst[j]:
                break
            j +=1
        if j == len(lst):
            return lst[i]

# Better way

def findFirstUnique_better(lst):
    mymap = OrderedDict()
    for i in lst:
        if i in mymap:
            mymap[i].append(1)
        else:
            mymap[i] = [1]
    for key, value in mymap.items():
        if len(value) == 1:
            return key

# Without using collections

def findFirstUnique_withoutOrderedDict(lst):
    mymap= dict()
    for i in lst:
        if i in mymap:
            del mymap[i]
        else:
            mymap[i] = lst.index(i)
    unique = None
    min = None
    for key, value in mymap.items():
        if min is None:
            min = value
            unique = key
            continue
        if value < min:
            min = value
            unique = key
    return unique


class TestFindFirstUnique(unittest.TestCase):

    def setUp(self) -> None:
        self.arr= [9,2,3,2,6,6]
        self.actual_output = 9

    def test_findFirstUnique_intuitive_success1(self):
        result = findFirstUnique_intuitive(self.arr)
        self.assertEqual(result, self.actual_output)

    def test_findFirstUnique_intuitive_success2(self):
        arr = [-1, 2, -1, 3, 2]
        result = findFirstUnique_intuitive(arr)
        self.assertEqual(result, 3)

    def test_findFirstUnique_better(self):
        result = findFirstUnique_better(self.arr)
        self.assertEqual(result, self.actual_output)

    def test_findFirstUnique_better2(self):
        arr = [4, 5, 1, 2, 0, 4]
        start = time.process_time()
        result = findFirstUnique_better(arr)
        print("Execution time: ", time.process_time() - start/1000, " ms")
        self.assertEqual(result, 5)

    def test_findFirstUnique_better3(self):
        arr = [4, 5, 1, 2, 0, 4]
        start = time.process_time()
        result = findFirstUnique_withoutOrderedDict(arr)
        print("Execution time: ", time.process_time() - start/1000, " ms")
        self.assertEqual(result, 5)

    def test_findFirstUnique_better4(self):
        arr = [-1, 2, -1, 3, 2]
        start = time.process_time()
        result = findFirstUnique_withoutOrderedDict(arr)
        print("Execution time: ", time.process_time() - start/1000, " ms")
        self.assertEqual(result, 3)

if __name__ == '__main__':
    unittest.main()











