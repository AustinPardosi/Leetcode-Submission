class Solution:
    def maxProfit(self, prices: List[int]) -> int: 
        # Two pointers, left = min, right = max
        l, r = 0, 1
        maxVal = 0

        while r < len(prices):
            diff = prices[r]-prices[l]
            maxVal = max(diff, maxVal)
            if diff < 0:
                l = r
            r += 1
        return maxVal

# Another Approach
class Solution:
    def maxProfit(self, prices: List[int]) -> int: 
        minVal = math.inf
        maxVal = 0

        for price in prices:
            minVal = min(price, minVal)
            maxVal = max((price-minVal), maxVal)
        return maxVal