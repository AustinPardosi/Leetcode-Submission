class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        valHistory = set()
        for num in nums:
            if num in valHistory:
                return num
            valHistory.add(num)
