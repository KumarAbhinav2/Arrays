"""
Given an array of integers arr, a lucky integer is an integer which has a frequency in the array equal to its value.

Return a lucky integer in the array. If there are multiple lucky integers return the largest of them.
If there is no lucky integer return -1.

Input: arr = [2,2,3,4]
Output: 2
Explanation: The only lucky number in the array is 2 because frequency[2] == 2.
"""

class Solution:

    def intuitive(self, arr) -> int:
        res = []
        count = 1
        n = len(arr)
        i = 1
        while i < n:
            if arr[i - 1] == arr[i]:
                count += 1
                i += 1
                continue
            elif count == arr[i-1]:
                res.append(count)
                count = 1
            i+=1
        if not res: return -1
        return res[-1]

    def pythonic(self, arr):
        import collections
        counter = collections.Counter(arr)
        ans = -1
        for k, v in counter.items():
            if k == v:
                ans = max(ans, k)
        return ans

    def python_v2(self, arr):
        import collections
        return max([-1] + [k for k,v in collections.Counter(arr).items() if k == v])

    def another(self, arr):
        out = -float("INF")
        counter = {}
        for num in arr:
            counter[num] = counter.setdefault(num, 0) + 1
        for num in counter:
            if counter[num] == num:
                out = max(out, num)
        if out == -float("INF"):
            return -1

        return out



