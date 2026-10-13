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

# ANOTHER
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1

        while left <= right:
            mid = (left+right)//2
            if nums[mid] == target:
                return mid

            # One of them must be sorted array
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid-1
                else:
                    left = mid+1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid+1
                else:
                    right = mid-1
        
        return -1