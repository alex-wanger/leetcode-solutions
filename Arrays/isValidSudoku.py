from collections import defaultdict
from typing import List
def isValidSudoku():
    board = [["1","2",".",".","3",".",".",".","."],  ["4",".",".","5",".",".",".",".","."],  [".","9","8",".",".",".",".",".","3"],  ["5",".",".",".","6",".",".",".","4"],  [".",".",".","8",".","3",".",".","5"],  ["7",".",".",".","2",".",".",".","6"],  [".",".",".",".",".",".","2",".","."],  [".",".",".","4","1","9",".",".","8"],  [".",".",".",".","8",".",".","7","9"]]
    rows = defaultdict(set)
    cols = defaultdict(set)
    square = defaultdict(set)
    for row in range(9):
        for col in range(9):
            curr = board[row][col]
            if (curr == "."):
                continue
            if (curr in rows[row]):
                return False
            if (curr in cols[col]):
                return False
            if (curr in square[row // 3 , col // 3]):
                return False

            cols[col].add(board[row][col])
            rows[row].add(board[row][col])
            square[(row // 3, col // 3)].add(board[row][col])
    return True