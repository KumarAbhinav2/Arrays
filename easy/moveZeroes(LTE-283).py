"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the
relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""

class Solution:

    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start = 0
        end = len(nums)-1
        while start <=end:
            if not nums[start]:
                nums.pop(start)
                nums.append(0)
                end -=1
            else:
                start+=1
        return nums

    def moveZeroes2(self, nums):
        slow = fast = 0
        while fast < len(nums):
            if nums[fast] != 0:
                if slow != fast:
                    nums[slow] = nums[fast]
                    nums[fast] = 0
                slow += 1
            fast += 1


obj = Solution()
print(obj.moveZeroes2([0,1,0,3,12]))
