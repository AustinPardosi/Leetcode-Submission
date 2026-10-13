class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        l, r = max(nums), sum(nums)

        while l<r:
            mid = (l+r) // 2

            # Greedily count groups with maximum currentSum = mid
            group = 1
            currentSum = 0
            for num in nums:
                if currentSum + num > mid:
                    group += 1
                    currentSum = num
                else:
                    currentSum += num
            
            if group <= k: # mid is too big, then small the right one
                r = mid
            else:
                l = mid + 1
        return l