"""
An image is represented by a 2-D array of integers, each integer representing the pixel value of the image
(from 0 to 65535).

Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill,
and a pixel value newColor, "flood fill" the image.

To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally
to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally
to those pixels (also with the same color as the starting pixel), and so on. Replace the color of all of
the aforementioned pixels with the newColor.

At the end, return the modified image.

Example 1:
Input:
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation:
From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected
by a path of the same color as the starting pixel are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected
to the starting pixel.
"""

class Solution:
    def floodFill(self, image, sr, sc, newColor):
        if not image:
            return None
        oldColor = image[sr][sc]
        # If the new color is equal to the old color
        if newColor == oldColor:
            return image
        # all possible 4 directions
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        def dfs(r, c):
            # new point should be of old color
            if image[r][c] == oldColor:
                # assign new color
                image[r][c] = newColor
                for i, j in directions:
                    nr = i+r
                    nc = j+c
                    if 0<=nr<len(image) and 0<=nc<len(image[0]):
                        dfs(nr, nc)
        dfs(sr, sc)
        return image

    # Time Complexity: O(N) number of pixels in the image
    # Space Complexity: O(N) size of the implicit call stack when calling dfs

