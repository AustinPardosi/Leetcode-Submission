class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binarySearch(start, end):
            # Basis Jika Interval Tidak Valid
            if start > end:
                return -1

            middle = (start + end) // 2
            if target == nums[middle]:
                return middle

            # Cek keterurutan (sisi kiri terurut)
            if nums[start] <= nums[middle]:
                if nums[start] <= target < nums[middle]:
                    return binarySearch(start, middle)
                else:
                    return binarySearch(middle + 1, end)

            # Cek keterurutan (sisi kanan terurut)
            else:
                if nums[middle] < target <= nums[end]:
                    return binarySearch(middle + 1, end)
                else:
                    return binarySearch(start, middle)

        return binarySearch(0, len(nums) - 1)
