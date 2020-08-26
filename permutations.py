class Solution:
    def permute(self, nums):
        visited = set()
        res = []
        self.backtracking(res, visited, [], nums)
        return res

    def backtracking(self, res, visited, subset, nums):
        if len(subset) == len(nums):
            res.append(subset)
        for i in range(len(nums)):
            if i not in visited:
                visited.add(i)
                self.backtracking(res, visited, subset + [nums[i]], nums)
                visited.remove(i)

obj = Solution()
print(obj.permute([1, 2, 3]))