class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        data = 0
        for num in nums:
            data ^= num
        return data