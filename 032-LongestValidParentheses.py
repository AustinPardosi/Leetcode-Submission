# Stack Approach
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]  # Base index before a possible valid substring
        result = 0

        for i, char in enumerate(s):
            if char == "(":
                stack.append(i)
            else:
                stack.pop()

                if not stack:
                    # This ')' cannot be matched; reset the base index
                    stack.append(i)
                else:
                    # Current valid substring length
                    result = max(result, i - stack[-1])

        return result