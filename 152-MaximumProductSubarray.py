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
