class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def recursive(start, end):
            # Basis Rekursif
            if start > end:
                return -1

            middle = (start + end) // 2
            if nums[middle] == target:
                return middle

            if nums[middle] > target:
                return recursive(start, middle - 1)

            if nums[middle] < target:
                return recursive(middle + 1, end)

        return recursive(0, len(nums) - 1)
