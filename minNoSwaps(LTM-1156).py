"""
Given a binary array data, return the minimum number of swaps required to group all 1’s
present in the array together in any place in the array.

Input: data = [1,0,1,0,1]
Output: 1
Explanation:
There are 3 ways to group all 1's together:
[1,1,1,0,0] using 1 swap.
[0,1,1,1,0] using 2 swaps.
[0,0,1,1,1] using 1 swap.
The minimum is 1.
"""

class Solution:

    def minSwaps(self, data):
        # window size
        ones = sum(data)
        # initializing max ones
        max_ones = sum(data[:ones])
        # current window count
        curr_ones = max_ones
        for i in range(ones, len(data)):
            # sliding window and checking window ones
            curr_ones += data[i] - data[i-ones]
            max_ones = max(max_ones, curr_ones)
        return ones-max_ones

    # Time Complexity : O(n)
    # Space Complexity: O(1)

