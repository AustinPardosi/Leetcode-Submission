# Brute Force — O(n²) time, O(n) space
class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        # Initialize every answer to 0.
        # If no warmer day exists, the answer stays 0.
        answer = [0] * len(temperatures)

        # Check each day
        for i in range(len(temperatures)):
            # Look at every future day to find a warmer temperature
            for j in range(i + 1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    # Found the first warmer day.
                    # The difference between indices is the waiting time.
                    answer[i] = j - i
                    break  # Stop searching; we need the FIRST warmer day.

        return answer


# Monotonic Stack — O(n) time, O(n) space
class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)

        # Initialize every answer to 0.
        # Days without a warmer future temperature remain 0.
        result = [0] * n

        # Store indices of days still waiting for a warmer temperature.
        # The temperatures at these indices decrease from bottom to top.
        # In Python, the top of the stack is the RIGHT side.
        stack = []

        # Process each day from left to right
        for i in range(n):

            # If today's temperature is warmer than the temperature
            # at the top of the stack, today's day resolves that old day.
            # Keep popping while today's temperature is warmer.
            while stack and temperatures[i] > temperatures[stack[-1]]:

                # Remove the most recent unresolved day from the stack
                idx = stack.pop()

                # Calculate how many days this day waited for a warmer day.
                # i = current day; idx = previous day.
                result[idx] = i - idx

            # Add today's index to the top of the stack.
            # Today may need to wait for a warmer temperature in the future.
            stack.append(i)

        # Any unresolved days keep their default answer of 0.
        return result