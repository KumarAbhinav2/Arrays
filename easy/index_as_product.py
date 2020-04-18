"""
Implement a function which modifies a list so that each index has a product of all the numbers present in the list
except the number stored at that index.

Input - arr = [1,2,3,4]
Output  - arr = [24,12,8,6]
"""
import unittest

# Intuitive way

def findProduct_intuitive(arr):
    result = []
    for i in range(len(arr)):
        temp = arr.pop(i)
        p = 1
        for j in arr:
            p *=j
        result.insert(i, p)
        arr.insert(i, temp)
    return result

# Better way

def findProduct_better(lst):
    left = 1
    product = []
    for ele in lst:
        product.append(left)
        left = left * ele
    # get product starting from right
    right = 1
    for i in range(len(lst)-1, -1, -1):
        product[i] = product[i] * right
        right = right * lst[i]
    return product


class TestIndexAsProduct(unittest.TestCase):

    def setUp(self) -> None:
        self.arr= [1,2,3,4]
        self.actual_output = [24,12,8,6]

    def test_findProduct_intuitive(self):
        result = findProduct_intuitive(self.arr)
        self.assertEqual(result, self.actual_output)

    def test_findProduct_better(self):
        result = findProduct_better(self.arr)
        self.assertEqual(result, self.actual_output)


if __name__ == '__main__':
    unittest.main()