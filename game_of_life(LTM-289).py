"""
According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by
the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0).
Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state.
The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.
"""


class Solution:

    def gameOfLife(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        # There are maximum 8 possible neighbours for given cell
        nbrs = [(1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1)]
        rows = len(board)
        cols = len(board[0])
        # Create a copy of the original board
        board_org = [row[:] for row in board]
        # Iterate through board cell by cell.
        for row in range(rows):
            for col in range(cols):
                # get live neighbours.
                l_nbr = 0
                for nbr in nbrs:
                    r = (row + nbr[0])
                    c = (col + nbr[1])
                    if (r < rows and r >= 0) and (c < cols and c >= 0) and (board_org[r][c]== 1):
                        l_nbr += 1
                # Rule 1 or Rule 3
                if board_org[row][col] == 1 and (l_nbr < 2 or l_nbr > 3):
                    board[row][col] = 0
                # Rule 4
                if board_org[row][col] == 0 and l_nbr == 3:
                    board[row][col] = 1

    def gameOfLife2(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        nbrs = [(1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1)]
        rows = len(board)
        cols = len(board[0])
        # Iterate through board cell by cell.
        for row in range(rows):
            for col in range(cols):
                # get live neighbours.
                l_nbr = 0
                for nbr in nbrs:
                    r = (row + nbr[0])
                    c = (col + nbr[1])
                    if (r < rows and r >= 0) and (c < cols and c >= 0) and (abs(board[r][c])== 1):
                        l_nbr += 1
                # Rule 1 or Rule 3
                if board[row][col] == 1 and (l_nbr < 2 or l_nbr > 3):
                    board[row][col] = -1
                # Rule 4
                if board[row][col] == 0 and l_nbr == 3:
                    board[row][col] = 2

        for row in range(rows):
            for col in range(cols):
                if board[row][col] > 0:
                    board[row][col] = 1
                else:
                    board[row][col] = 0


obj = Solution()
board =[
          [0,1,0],
          [0,0,1],
          [1,1,1],
          [0,0,0]
]
obj.gameOfLife(board)

