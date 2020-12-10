"""
You are given a m x n 2D grid initialized with these three possible values.

-1 - A wall or an obstacle.
0 - A gate.
INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF
as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate.
If it is impossible to reach a gate, it should be filled with INF.
"""


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.

        Algo:
        1) Consider the rooms array as undirected graph
        2) Get the spare queue
        3) for i in rows:
            for j in cols:
                if room is gate:
                    queue.add(room)
        4) while queue is not empty:
            queue.pop(first gate)
            do bfs i.e check for rooms in 1 space in all directions [(1, 0), (-1, 0), (0, 1), (0, -1)]
            if new room is not wall or not 0:
                queue.add(new room)
        """
        if not rooms: return
        from collections import deque
        q = deque()
        rows = len(rooms)
        cols = len(rooms[0])
        gate = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        empty = 2147483647
        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == gate:
                    q.append((r, c))

        while q:
            i, j = q.popleft()
            for r, c in directions:
                nr = r + i
                nc = c + j
                if 0 <= nr <= rows - 1 and 0 <= nc <= cols - 1 and rooms[nr][nc] == empty:
                    rooms[nr][nc] = rooms