# Brute Force = DFS = Time Complexity (O(2**n))
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        def dfs(i, j):
            # We matched every character in t: one valid way
            if j == len(t):
                return 1

            # We ran out of characters in s before finishing t
            if i == len(s):
                return 0

            # Option 1: Skip the current character in s
            count = dfs(i + 1, j)

            # Option 2: Take the current character if it matches
            if s[i] == t[j]:
                count += dfs(i + 1, j + 1)

            return count

        return dfs(0, 0)
