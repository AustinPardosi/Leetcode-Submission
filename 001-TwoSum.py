class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i, num in enumerate(nums):
            temp = target - num
            if temp in hashMap:
                return hashMap[temp], i
            hashMap[num] = i
        return
