
class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        # Brute Force: O(m * n) time, O(m * n) extra space

        nRow, nCol = len(matrix), len(matrix[0])

        # Directions: Right -> Down -> Left -> Up
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        direction = 0  # Start by moving right

        row, col = 0, 0  # Start at the top-left cell
        result = []
        visited = set()  # Track cells that have already been visited

        # Visit every cell in the matrix exactly once
        for _ in range(nRow * nCol):
            # Add the current cell's value to the result
            result.append(matrix[row][col])

            # Mark the current cell as visited
            visited.add((row, col))

            # Calculate the next cell in the current direction
            dr, dc = directions[direction]
            nextRow, nextCol = row + dr, col + dc

            # If the next cell is outside the matrix
            # or has already been visited, turn clockwise
            if (
                nextRow < 0 or nextRow >= nRow
                or nextCol < 0 or nextCol >= nCol
                or (nextRow, nextCol) in visited
            ):
                # Move to the next direction:
                # Right -> Down -> Left -> Up -> Right
                direction = (direction + 1) % 4

                # Recalculate the next cell after turning
                dr, dc = directions[direction]
                nextRow, nextCol = row + dr, col + dc

            # Move to the next cell
            row, col = nextRow, nextCol

        return result