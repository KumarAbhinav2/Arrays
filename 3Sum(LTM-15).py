"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

Notice that the solution set must not contain duplicate triplets.



Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
"""

class Solution:

    def twoSum(self, nums, i, res):
        lo = 0
        hi = len(nums)-1
        while lo < hi:
            c_sum = nums[i] + nums[lo] + nums[hi]
            if c_sum < 0:
                lo +=1
            elif c_sum > 0:
                hi -=1
            else:
                res.append([nums[i], nums[lo], nums[hi]])
                lo+=1
                hi-=1
                while lo < hi and nums[lo] == nums[lo-1]:
                    lo+=1

    def threeSum(self, nums):
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i]>0:
                break
            elif i == 0 or nums[i-1] != nums[i]:
                self.twoSum(nums, i, res)