"""
Given an absolute path for a file (Unix-style), simplify it. Or in other words, convert it to the canonical path.

In a UNIX-style file system, a period '.' refers to the current directory.
Furthermore, a double period '..' moves the directory up a level.

Note that the returned canonical path must always begin with a slash '/', and
there must be only a single slash '/' between two directory names.
The last directory name (if it exists) must not end with a trailing '/'.
Also, the canonical path must be the shortest string representing the absolute path.



Example 1:

Input: path = "/home/"
Output: "/home"
Explanation: Note that there is no trailing slash after the last directory name.
Example 2:

Input: path = "/../"
Output: "/"
Explanation: Going one level up from the root directory is a no-op, as the root level is the highest level you can go.
Example 3:

Input: path = "/home//foo/"
Output: "/home/foo"
Explanation: In the canonical path, multiple consecutive slashes are replaced by a single one.
Example 4:

Input: path = "/a/./b/../../c/"
Output: "/c"
"""

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        # split the path by /
        for char in path.split('/'):
            # if . then no need to do anything and if found '' as well don't do anything
            if char == '.' or not char:
                continue
            # pop one elem out when found .., as we need to move one directory up
            elif char == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(char)
        # extra /  for having root added at the beginning
        return '/'+'/'.join(stack)

    # Time complexity: O(n)
    # space Complexity: O(2n), one for array and another one for string =~ O(n)