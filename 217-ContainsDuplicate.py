class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dataSet = set()
        for num in nums:
            if num in dataSet:
                return True
            dataSet.add(num)
        return False
