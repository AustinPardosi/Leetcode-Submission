class Solution:
    def findMin(self, nums: List[int]) -> int:
        def binarySearch(start, end):
            # Basis jika hanya ada 1 element
            if start == end:
                return nums[start]

            # Kalau sudah terurut
            if nums[start] < nums[end]:
                return nums[start]

            middle = (start + end) // 2

            if nums[middle] > nums[end]:
                return binarySearch(middle + 1, end)
            else:
                return binarySearch(start, middle)

        return binarySearch(0, len(nums) - 1)
