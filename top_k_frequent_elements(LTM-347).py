"""
Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
"""

import heapq
from collections import Counter

class Solution:

    def topKFrequent(self, nums, k):
        # O(n) = 1
        if len(nums) == k:
            return nums
        # O(n) = n
        hashmap = Counter(nums)
        # O(nlogk)
        return heapq.nlargest(k, hashmap.keys(), key=hashmap.get)

    def topKFrequent_quickSelect(self, nums, k):

        from random import randint
        count = Counter(nums)
        unique = list(count.keys())

        def partition(left, right, pivot_index):
            pivot_freq = count.get(unique[pivot_index])
            unique[pivot_index], unique[right] = unique[right], unique[pivot_index]
            store = left

            for i in range(left, right):
                if count.get(unique[i]) < pivot_freq:
                    unique[store], unique[i] = unique[i], unique[store]
                    store += 1

            unique[right], unique[store] = unique[store], unique[right]
            return store

        def select(left, right, kth_smallest):
            if left == right:
                return

            pivot_index = randint(left, right)

            pivot_index = partition(left, right, pivot_index)

            if kth_smallest == pivot_index:
                return

            if kth_smallest < pivot_index:
                select(left, pivot_index - 1, kth_smallest)
            else:
                select(pivot_index + 1, right, kth_smallest)

        n = len(unique)
        select(0, n - 1, n - k)
        return unique[n - k:]

        ## Time Complexity O(n) in average case, O(n^2) in worst case
        ## Space Complexity O(n) to hashmap and array of unique elements

