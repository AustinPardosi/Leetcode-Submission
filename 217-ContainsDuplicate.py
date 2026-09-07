class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        data = set()
        for num in nums:
            if num in data:
                return True
            data.add(num)
        return False