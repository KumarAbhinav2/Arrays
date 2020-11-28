"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the
following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Input: board =
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
"""

class Solution:

    def isValidSudoko(self, board):
        rows = [{} for i in range(9)]
        cols = [{} for i in range(9)]
        boxes = [{} for i in range(9)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != '.':
                    num = int(num)
                    b = (i//3)*3+j//3
                    rows[i][num] = rows[i].get(num, 0) + 1
                    cols[j][num] = cols[j].get(num, 0) + 1
                    boxes[b][num] = boxes[b].get(num, 0)+1

                    if rows[i][num] > 0 or cols[j][num] > 0 or boxes[j][num] > 0:
                        return False
        return True

        ## Time complexity: O(1)
        ## Space complexity: O(1)