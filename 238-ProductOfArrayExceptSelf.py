class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftArr = [1]*len(nums)
        for i in range (1, len(nums)):
            leftArr[i] = leftArr[i-1] * nums[i-1]
        
        rightArr = [1]*len(nums)
        for i in range (len(nums)-2, -1, -1):
            rightArr[i] = rightArr[i+1] * nums[i+1]

        result = [1] * len(nums)
        for i in range(len(nums)):
            result[i] = leftArr[i] * rightArr[i]
        
        return result
