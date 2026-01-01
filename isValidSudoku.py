from typing import List


def isValidSudoku():
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], ["4", ".", ".", "8",
                                                                                                                                                                                                          ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

    rows = []

    for i in range(len(board)):
        hashset = set()
        row = board[i]
        rows.append(row)
        for number in row:
            if (number == "."):
                continue
            elif number in hashset:
                return False
            else:
                hashset.add(number)

    # [5,3, .] row 0 index 0
    # [5,3, .]
    # [5,3, .]
    for j in range(9):  # For each column
        seen = set()
        for i in range(9):  # For each row
            number = board[i][j]
            if number == ".":
                continue
            if number in seen:
                return False
            seen.add(number)

    for i in range(9):
        for row in range(3):
            for column in range(3):
                board[row][column]

        # 0, 0 1,0 2,0
        # 1, 0, 1,1 2,1
        # 2 0, 2,1 2,2

    return True


isValidSudoku()
