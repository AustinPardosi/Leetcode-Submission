class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMin, curMax = 1, 1

        for num in nums:
            if num == 0:
                curMin, curMax = 1, 1
                continue
            temp = num * curMax
            curMax = max(num * curMax, num * curMin, num)
            curMin = min(temp, num * curMin, num)
            res = max(curMax, res)

        return res

# DP Approach
class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        n = len(nums)

        # Maximum/minimum product of a subarray ending at each position
        max_dp = [0] * (n + 1)
        min_dp = [0] * (n + 1)
        max_dp[1] = min_dp[1] = result = nums[0]

        for i in range(2, n + 1):
            num = nums[i - 1]

            # Consider starting fresh or extending the previous max/min product
            max_dp[i] = max(num, max_dp[i - 1] * num, min_dp[i - 1] * num)
            min_dp[i] = min(num, max_dp[i - 1] * num, min_dp[i - 1] * num)

            # Track the best product found anywhere
            result = max(result, max_dp[i])

        return result