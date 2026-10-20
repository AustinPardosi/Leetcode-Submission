# Brute Force
class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        result = 0

        for i in range(len(heights)):
            min_height = float("inf")

            for j in range(i, len(heights)):
                min_height = min(min_height, heights[j])

                area = min_height * (j - i + 1)
                result = max(area, result)

        return result

# Monotonic Stack: O(n) time, O(n) space
class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        area = 0
        stack = []  # Store indices, not heights

        for i in range(len(heights) + 1):
            # Use a virtual bar of height 0 to clear the stack at the end
            height = heights[i] if i < len(heights) else 0

            # If the current bar is shorter, calculate the popped bar's area
            while stack and height < heights[stack[-1]]:
                # Pop the index of the bar whose rectangle we're calculating
                idx = stack.pop()
                val = heights[idx]

                # Find the nearest shorter bar on the left
                left_boundary = stack[-1] if stack else -1

                # Calculate the width between the two shorter boundaries
                width = i - left_boundary - 1

                # Update the largest area found so far
                area = max(area, width * val)

            # Store the current bar's index
            stack.append(i)

        return area
