class Solution:
    def help(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        # rob1, rob2, n, n+1
        for n in nums:
            temp = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = temp

        return rob2

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.help(nums[1:]), self.help(nums[:-1]))

## DP APPROACH
class Solution:
    def rob(self, nums: List[int]) -> int:
        # Edge case: only one house
        if len(nums) == 1:
            return nums[0]

        # Case 1: exclude the first house
        no_first = self.rob_linear(nums[1:])

        # Case 2: exclude the last house
        no_last = self.rob_linear(nums[:-1])

        # Return the better result from both cases
        result = max(no_first, no_last)
        return result

    
    def rob_linear(self, nums):
        n = len(nums)
        # dp[i] = maximum money robbed from the first i houses
        dp = [0] * (n + 1)
        dp[1] = nums[0]

        for i in range(2, n+1):
            # Skip the current house or rob it and skip the previous house
            dp[i] = max(dp[i-1], nums[i-1] + dp[i-2])
        return dp[n]