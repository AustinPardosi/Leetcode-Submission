# Greedy — Optimal approach
# Time: O(n) — visit each price once
# Space: O(1) — use only one variable
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        result = 0

        for i in range(1, len(prices)):
            # If today's price is higher than yesterday's,
            # add the profit from this price increase.
            if prices[i] > prices[i - 1]:
                result += prices[i] - prices[i - 1]

        return result
