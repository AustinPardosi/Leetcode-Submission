class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        n = len(nums)
        # dp[i] = length of the longest increasing subsequence ending at nums[i]
        # Every number alone forms a subsequence of length 1
        dp = [1] * n

        for i in range(n):
            for j in range(i):
                # nums[j] must be smaller than nums[i] to extend an increasing subsequence
                if nums[i] > nums[j]:
                    # Extend the subsequence ending at nums[j] by adding nums[i]
                    dp[i] = max(dp[i], dp[j]+1)
        # The longest increasing subsequence can end at any index
        return max(dp)