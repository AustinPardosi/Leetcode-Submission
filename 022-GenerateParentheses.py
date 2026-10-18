class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []

        def backtrack(current, open_count, close_count):
            # Base case: string is full length (n pairs = 2n chars).
            # Our rules guarantee it's valid, so just save it.
            if len(current) == 2 * n:
                result.append(current)
                return

            # Choice 1: add "(" if we still have opens left in the budget
            if open_count < n:
                backtrack(current + "(", open_count + 1, close_count)

            # Choice 2: add ")" only if there's an unmatched "(" to close
            if close_count < open_count:
                backtrack(current + ")", open_count, close_count + 1)

        # Start with an empty string, nothing opened or closed yet
        backtrack("", 0, 0)
        return result