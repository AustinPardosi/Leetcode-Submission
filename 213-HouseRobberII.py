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
