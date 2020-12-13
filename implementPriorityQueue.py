"""
Implement Priority Queue with insert, extract_min and decrease_key methods
"""
import sys

class Node:
    def __init__(self, val, key):
        self.val = val
        self.key = key

class PriorityQueue:
    def __init__(self):
        self.queue = []

    def __len__(self):
        return len(self.queue)

    def insert(self, node):
        self.queue.append(node)
        return self.queue[-1]

    def extract_min(self):
        if not self.queue: return None
        min_so_far, min_index = sys.maxsize, sys.maxsize
        for index, node in enumerate(self.queue):
            if node.key < min_so_far:
                min_so_far = node.key
                min_index = index
        return self.queue.pop(min_index)

    def decrease_key(self, val, new_key):
        for node in self.queue:
            if node.val == val:
                node.key = new_key
                return node
        return None




