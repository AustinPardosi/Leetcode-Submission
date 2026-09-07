class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        data = {}
        for i, num in enumerate(nums):
            if num in data and (i-data[num] <= k) :
                return True
            data[num] = i
        return False
