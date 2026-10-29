# Brute Force
# Time Complexity: O(n^2)
# Space Complexity: O(n) for the result array
class Solution:
    def canSeePersonsCount(self, heights: list[int]) -> list[int]:
        n = len(heights)
        result = []

        for i in range(n):
            count = 0
            maxHeight = 0

            # Check every person to the right of person i
            for j in range(i + 1, n):

                # A person is visible if they are taller than
                # everyone between person i and person j
                if heights[j] > maxHeight:
                    count += 1
                    maxHeight = heights[j]

                # The first person as tall as or taller than
                # person i is also visible, but blocks everyone behind them
                if heights[j] >= heights[i]:
                    break

            result.append(count)

        return result

# Monotonic Stack
# Time Complexity: O(n)
# Space Complexity: O(n) for the stack and result array
class Solution:
    def canSeePersonsCount(self, heights: list[int]) -> list[int]:
        n = len(heights)
        result = [0] * n
        stack = []

        # Traverse from right to left so we can check
        # the people who are already to the current person's right
        for i in range(n - 1, -1, -1):

            # Every shorter person on top of the stack is visible.
            # Remove them because the current person blocks them
            # from being relevant to people further left.
            while stack and heights[stack[-1]] < heights[i]:
                stack.pop()
                result[i] += 1

            # If someone remains, they are taller than or equal
            # to the current person. They are also visible,
            # but block everyone behind them.
            if stack:
                result[i] += 1

            # Store the current person's index for people further left
            stack.append(i)

        return result
