"""
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Note: The algorithm should run in linear time and in O(1) space.

Example 1:

Input: [3,2,3]
Output: [3]
Example 2:

Input: [1,1,1,3,3,2,2,2]
Output: [1,2]
"""

class Solution:

    def majorityElement1(self, nums):
        t = len(nums)//3
        res = set()
        mymap = {}
        for i in nums:
            if i in mymap:
                mymap[i] +=1
                if i in res:
                    continue
                if mymap[i] > t:
                    res.add(i)
            else:
                mymap[i] = 1
        for i, v in mymap.items():
            if v > t:
                res.add(i)
        return res

    def majorityElement2(self, nums):
        myset = set(nums)
        t = len(nums)//3
        res = []
        for i in myset:
            if nums.count(i) > t:
                res.append(i)
        return res

