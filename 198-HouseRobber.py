class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        # [rob1, rob2, n, n+1]
        for n in nums:
            temp = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = temp

        return rob2

# DP APPROACH
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        # dp[i] = maximum money we can rob from the first i houses
        dp = [0] * (n + 1)
        # Base case: if we only have one house, rob it
        dp[1] = nums[0]

        # Calculate the maximum money for the first i houses
        for i in range(2, n+1):
            # Option 1: Skip the current house, keeping the best result from the previous house -> dp[i-1]
            # Option 2: Rob the current house -> nums[i-1] , adding its money to the best result from houses before the previous one -> dp[i-2]
            # We cannot rob adjacent houses, so choose whichever option gives more money
            dp[i] = max(dp[i-1], nums[i-1] + dp[i-2])
        # Return the maximum money we can rob from all houses
        return dp[n]
