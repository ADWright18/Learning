"""
Problem Description: Determine if a 9x9 Sudoku board is valid.

Example:
Input:
[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]

Output:
True

Solution:
1. Create a dictionary to store {sorted(values) : [list of values]}
2. Add each row, column, and sub-box to their respective dictionaries
    - Convert the string lists -> integer lists
3. Iterate through each key
    - If the list of values contains a duplicate number - return False
4. Otherwise, return true
"""
class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        d = {} # Store each row

        # Check the rows
        for i in range(len(board)):
            current_row = []

            for j in range(len(board[i])):
                if (board[i][j] != "."):
                    current_row.append(board[i][j])

            sorted_row = ''.join(sorted(current_row))

            # Check if the current_row contains a duplicate value
            if (len(current_row) != len(set(current_row))):
                return False
            elif (sorted_row not in d):
                d[sorted_row] = current_row

        # Check the columns
        for i in range(len(board)):
            current_column = []

            for j in range(len(board[i])):
                if (board[j][i] != '.'):
                    current_column.append(board[j][i])

            sorted_column = ''.join(sorted(current_column))

            # Check if the current_column contains a duplicate value
            if (len(current_column) != len(set(current_column))):
                return False
            elif (sorted_column not in d):
                d[sorted_column] = current_column

        # Check the sub-boxes
        for i in range(0,2):
            n = 3 * i       # Start value
            m = 3 * (i + 1) # End value
            for j in range(len(board[n:m])):
