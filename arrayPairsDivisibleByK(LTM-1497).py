"""
Given an array of integers arr of even length n and an integer k.

We want to divide the array into exactly n / 2 pairs such that the sum of each pair is divisible by k.

Return True If you can find a way to do that or False otherwise.
Example 1:

Input: arr = [1,2,3,4,5,10,6,7,8,9], k = 5
Output: true
Explanation: Pairs are (1,9),(2,8),(3,7),(4,6) and (5,10).
Example 2:

Input: arr = [1,2,3,4,5,6], k = 7
Output: true
Explanation: Pairs are (1,6),(2,5) and(3,4).
Example 3:

Input: arr = [1,2,3,4,5,6], k = 10
Output: false
Explanation: You can try all possible pairs to see that there is no way to divide
arr into 3 pairs each with sum divisible by 10.
"""

class Solution:
    def canArrange(self, arr, k):
        # array to hold pairs
        count = [0] * k
        for num in arr:
            count[num%k] += 1
        for i in range(k):
            # because we know as given condition (i + j) % k == 0
            j = -i % k
            while count[i] > 0:
                count[i] -=1
                count[j] -=1
                # decrementing both the pairs from the array
                if count[j] < 0:
                    # if we don't have pair
                    return False
        return True

    def canArrange_better(self, arr, k):
        # array to hold pairs
        count = [0] * k
        for num in arr:
            count[num%k] += 1
        if count[0] % 2: return False
        i, j = 1, k-1
        while i < j:
            if count[i] != count[j]:
                return False
            i+=1
            j-=1
        return True


# Time Complexity: O(n)
# Space Complexity: O(k)


