"""
Given an integer array nums, find the contiguous subarray (containing at least one number)
which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
"""

class Solution:

    def maxSubArray(self, a):

        max_so_far = a[0]
        curr_max = a[0]

        for i in range(1, len(a)):
            curr_max = max(a[i], curr_max + a[i])
            max_so_far = max(max_so_far, curr_max)

        return max_so_far

    def maxSubArray2(self, nums):
        dp = [0]*len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1]+nums[i], nums[i])
        return max(dp)


obj = Solution()
print(obj.maxSubArray([6, 3, -1, -3, 4, -2, 2, 4, 6, -12, -7]))
print(obj.maxSubArray2([6, 3, -1, -3, 4, -2, 2, 4, 6, -12, -7]))





























