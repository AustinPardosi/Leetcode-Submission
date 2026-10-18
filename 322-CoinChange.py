class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        INF = float("inf")
        # dp[i] = minimum number of coins needed to make amount i
        dp = [INF] * (amount + 1)
        dp[0] = 0 # Making amount 0 requires 0 coins

        for i in range(1, amount+1):
            for c in coins:
                if i >= c:
                    # Use coin c and add it to the minimum coins needed for amount i - c
                    dp[i] = min(dp[i], dp[i-c]+1)
        # Return -1 if the amount cannot be made using the given coins
        return dp[amount] if dp[amount] != INF else -1
