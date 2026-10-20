class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        n = len(s)
        data = set(wordDict)
        # dp[i] = can we break the first i characters into valid words?
        dp = [False] * (n + 1)
        # Starting point: we can always break an empty string
        dp[0] = True

        for i in range(1, n+1):
            for j in range(i):
                # If the prefix before j is valid
                # and s[j:i] is a valid word, we can reach i
                if dp[j] and s[j:i] in data:
                    dp[i] = True
        return dp[n]