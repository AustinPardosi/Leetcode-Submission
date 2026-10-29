# Backtracking + Sets
# Time Complexity: O(n!) 
# Space Complexity: O(n^2)

class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        # Create an empty n x n chessboard
        board = [["."] * n for _ in range(n)]
        result = []

        # Track columns and diagonals that already contain a queen
        col = set()
        posDia = set()  # row + col: one diagonal direction
        negDia = set()  # row - col: the other diagonal direction

        def backtracking(row):
            # Base case: queens have been placed in all n rows
            if row == n:
                # Convert each board row into a string and save this solution
                result.append(["".join(r) for r in board])
                return

            # Try placing a queen in every column of the current row
            for c in range(n):

                # Skip this position if another queen attacks it:
                # - Same column
                # - Same diagonal (row + col)
                # - Same diagonal (row - col)
                if (c in col or
                    row + c in posDia or
                    row - c in negDia):
                    continue

                # Place the queen at (row, c)
                board[row][c] = "Q"

                # Record the column and diagonals occupied by this queen
                col.add(c)
                posDia.add(row + c)
                negDia.add(row - c)

                # Recursively place a queen in the next row
                backtracking(row + 1)

                # Backtrack: remove the queen to try another column
                board[row][c] = "."

                # Remove this queen's column and diagonal records
                col.remove(c)
                posDia.remove(row + c)
                negDia.remove(row - c)

        # Start placing queens from the first row (row 0)
        backtracking(0)

        # Return all valid board arrangements
        return result