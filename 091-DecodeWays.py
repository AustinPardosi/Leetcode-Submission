class Solution:
    def numDecodings(self, s: str) -> int:
        # in case string kosong return 1
        history = {len(s): 1}

        def dfs(i):
            if i in history:
                return history[i]
            if s[i] == "0":
                return 0

            res = dfs(i + 1)
            if i + 1 < len(s) and (
                s[i] == "1" or (s[i] == "2" and s[i + 1] in "0123456")
            ):
                res += dfs(i + 2)

            history[i] = res
            return res

        return dfs(0)

# DP APPROACH
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        # dp[i] = number of ways to decode the first i characters
        dp = [0] * (n + 1)
        # Base case: an empty string has one way to decode
        dp[0] = 1
        # The first character can only be decoded if it is not "0"
        dp[1] = 1 if s[0] != "0" else 0

        for i in range(2, n+1):
            # Check if the last single digit is valid (1-9)
            one = s[i-1]
            # Check if the last two digits form a valid number (10-26)
            two = s[i-2:i]

            # If the last digit is valid, extend every decoding of the previous i-1 characters
            if one != "0":
                dp[i] += dp[i-1]
            
            # If the last two digits are valid, extend every decoding of the previous i-2 characters
            if "10" <= two <= "26":
                dp[i] += dp[i-2]

        # Return the number of ways to decode the entire string
        return dp[n]
