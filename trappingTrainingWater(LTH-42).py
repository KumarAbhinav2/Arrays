"""
Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
In this case, 6 units of rain water (blue section) are being trapped.

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
"""
"""
ALGO: (Hint: water is trapped between rightmost highest tower and leftmost highest , driving factor is minimum of them)
1) Iterate the list from leftside and get the list of leftmost highest towers of each tower(including current)
2) Iterate the list from rightside and get the list of rightmost highest tower of each tower (including current)
3) trapped water at each tower = min(leftmost, rightmost) - height of current tower
4) take lists generated from 1 and 2 and generate list of water trapped at each tower
5) sum of the elements is the answer
"""

from duration import duration
import unittest


class Solution:

    @duration
    def intuitive(self, arr):
        left_iter = []
        n = len(arr)
        curr_max = 0
        for i in arr:
            curr_max = max(curr_max, i)
            left_iter.append(curr_max)
        curr_max = 0
        right_iter = [0]*n
        for j in range(n-1, -1, -1):
            curr_max = max(curr_max, arr[j])
            right_iter[j] = curr_max
        res = 0
        for k in range(n):
            t_water = min(left_iter[k], right_iter[k]) - arr[k]
            res +=t_water
        return res

    @duration
    def shorter(self, arr):
        res = 0
        n = len(arr)
        for i in range(n):
            left_max = max(arr[:i+1])
            right_max = max(arr[i:])
            t_water = min(left_max, right_max) - arr[i]
            res +=t_water
        return res

    @duration
    def optimised(self, height):
        n = len(height)
        if n < 3:
            return 0
        res = 0
        i = 0
        j = n-1
        left_arr = height[0]
        right_arr = height[n-1]
        while i <= j:
            left_arr = max(left_arr, height[i])
            right_arr = max(right_arr, height[j])
            if left_arr <= right_arr:
                res += left_arr-height[i]
                i+=1
            else:
                res += right_arr-height[j]
                j-=1
        return res



class TestSolution(unittest.TestCase):

    def setUp(self) -> None:
        self.input1 = [0,1,0,2,1,0,1,3,2,1,2,1]
        self.output = 6
        self.obj = Solution()

    def test_using_array(self):
        res = self.obj.intuitive(self.input1)
        self.assertEqual(res, self.output)

    def test_using_array_optimised(self):
        res = self.obj.optimised(self.input1)
        self.assertEqual(res, self.output)

    def test_using_array_shorter(self):
        res = self.obj.shorter(self.input1)
        self.assertEqual(res, self.output)


if __name__ == '__main__':
        unittest.main()





