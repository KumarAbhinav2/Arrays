"""
Given an integer array nums, find three numbers whose product is maximum and return the maximum product.

Example 1:

Input: nums = [1,2,3]
Output: 6
Example 2:

Input: nums = [1,2,3,4]
Output: 24
"""
import heapq


class Solution:

    def maximumProduct(self, nums):
        if len(nums) == 3:
            return nums[0]*nums[1]*nums[2]

        max_3, min_3 = heapq.nlargest(3, nums), heapq.nsmallest(2, nums)
        return max(max_3[0]*max_3[1]*max_3[2], min_3[0]*min_3[1]*max_3[0])

    # Time complexity: O(Nlogk)