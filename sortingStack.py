"""
Sort a stack in decreasing order, we can use additional stack as buffer
"""

class Stack:

    def __init__(self):
        self._stack = []

    def is_empty(self):
        return not self._stack

    def pop(self):
        if not self.is_empty():
            return self._stack.pop()

    def peek(self):
        if not self.is_empty():
            return self._stack[-1]

    def push(self, elem):
        self._stack.append(elem)

    def sort(self):
        buff = Stack()
        while not self.is_empty():
            curr = self.pop()
            while not buff.is_empty() and curr < buff.peek():
                self.push(curr)
            buff.push(curr)
        return buff

    # Time Complexity: O(n^2)
    # Space Complexity: O(n)


