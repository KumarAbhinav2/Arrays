"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.



Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
"""
from collections import defaultdict


class Solution:

    def groupAnagrams(self, strs):
        res = defaultdict(list)
        for a in strs:
            sa = ''.join(sorted(a))
            res[sa].append(a)
        return [a for a in res.values()]