# Brute Force = DFS + Memoization (Top-Down DP)
# Time Complexity: O(m * n)
# Space Complexity: O(m * n)
# m = len(s), n = len(t)

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        data = {}

        def dfs(i, j):
            # We matched every character in t: one valid way
            if j == len(t):
                return 1

            # We ran out of characters in s before finishing t
            if i == len(s):
                return 0

            # Return the saved answer if we calculated this state before
            if (i, j) in data:
                return data[(i, j)]

            # Option 1: Skip the current character in s
            count = dfs(i + 1, j)

            # Option 2: Take the current character if it matches
            if s[i] == t[j]:
                count += dfs(i + 1, j + 1)

            # Save the answer for this state
            data[(i, j)] = count
            return count

        return dfs(0, 0)

# TODO : Dynamic Programming 2 Dimension