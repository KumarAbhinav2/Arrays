"""
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are
drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container,
such that the container contains the most water.

Notice that you may not slant the container.
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water
(blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
Example 3:

Input: height = [4,3,2,1,4]
Output: 16
"""


class Solution:
    def maxArea(self, height) -> int:
        i = 0
        j = len(height) - 1
        max_area = 0
        # Area will always be driven by the length of the smaller vertical line
        while i < j:
            if height[i] <= height[j]:
                cur_min_h = height[i]
                i += 1
            else:
                cur_min_h = height[j]
                j -= 1
            max_area = max(max_area, cur_min_h * (j - i + 1))
        return max_area

    # Time Complexity: O(n)
    # Space Complexity: O(1)