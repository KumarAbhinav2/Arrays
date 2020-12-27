"""
Given a binary array, find the maximum number of consecutive 1s in this array if you can flip at most one 0.

Example 1:
Input: [1,0,1,1,0]
Output: 4
Explanation: Flip the first zero will get the the maximum number of consecutive 1s.
    After flipping, the maximum number of consecutive 1s is 4.
"""

class Solution:
    def findMaxConsecutiveOnes(self, nums):
        # pre and curr for current and previous consecutive lengths separated by 0
        maxlen, pre, curr = 0, -1, 0
        for num in nums:
            # if we found 0 , we assign curr to prev and initialize curr = 0
            if num == 0:
                pre, curr = curr, 0
            else:
                curr +=1
            # the max would be previous + 1(0 flipped to 1) + current
            maxlen = max(maxlen, pre+1+curr)
        return maxlen