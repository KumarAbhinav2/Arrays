"""
Implement a function which modifies a list so that each index has a product of all the numbers present in the list
except the number stored at that index.

Input  - arr = [1,2,3,4]
Output - arr = [24,12,8,6]
"""

# lets not allow zero
from duration import duration
import unittest


class Solution:

    @duration
    def better1(self, arr):
        product = 1
        for i in arr:
            product *= i
        for index, i in enumerate(arr):
            arr[index] = product / i
        return arr

    @duration
    def intuitive(self, arr):
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

    @duration
    def better2(self, lst):
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
        self.obj = Solution()
        self.arr= [1,2,3, 4]
        self.actual_output = [24,12,8,6]

    def test_findProduct_intuitive(self):
        result = self.obj.intuitive(self.arr)
        self.assertEqual(result, self.actual_output)

    def test_findProduct_better1(self):
        result = self.obj.better1(self.arr)
        self.assertEqual(result, self.actual_output)

    def test_findProduct_better2(self):
        result = self.obj.better2(self.arr)
        self.assertEqual(result, self.actual_output)


if __name__ == '__main__':
    unittest.main()