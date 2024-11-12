class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        tempSum = 0

        for num in nums:
            if tempSum < 0:
                tempSum = 0
            tempSum += num
            maxSum = max(maxSum, tempSum)
        return maxSum
