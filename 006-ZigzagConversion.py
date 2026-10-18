class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # If there is only one row, nothing needs to change.
        if numRows == 1:
            return s

        # Create an empty string for each row.
        rows = [""] * numRows

        current_row = 0
        direction = 1  # 1 = down, -1 = up

        for char in s:
            # Put this character into the current row.
            rows[current_row] += char

            # If we reach the bottom, start moving up.
            if current_row == numRows - 1:
                direction = -1

            # If we reach the top, start moving down.
            elif current_row == 0:
                direction = 1

            # Move one row in the current direction.
            current_row += direction

        # Combine all rows into the final string.
        return "".join(rows)