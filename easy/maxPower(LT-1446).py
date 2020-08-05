"""
Given a string s, the power of the string is the maximum length of a non-empty substring that
contains only one unique character.

Return the power of the string.

Example 1:

Input: s = "leetcode"
Output: 2
Explanation: The substring "ee" is of length 2 with the character 'e' only.
Example 2:

Input: s = "abbcccddddeeeeedcba"
Output: 5
Explanation: The substring "eeeee" is of length 5 with the character 'e' only.
Example 3:

Input: s = "triplepillooooow"
Output: 5
Example 4:

Input: s = "hooraaaaaaaaaaay"
Output: 11
Example 5:

Input: s = "tourist"
Output: 1
"""


class Solution:

    def maxPower(self, s: str) -> int:
        l = 1
        res = 1
        for i in range(1,len(s)):
            if s[i-1] == s[i]:
                l+=1
                res = max(res,l)
            else:
                l = 1
        return res

    def maxPower_dp(self, s):
        dp = dict()
        max_power = 1
        prev = None
        for c in s:
            if c == prev:
                dp[c] +=1
                if dp[c] > max_power:
                    max_power = dp[c]
            else:
                dp[c] = 1
            prev = c
        return max_power

obj = Solution()
print(obj.maxPower("hooraaaaaaaaaaay"))
print(obj.maxPower_dp("hooraaaaaaaaaaay"))