
class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        # Brute Force: O(n) time, O(1) extra space
        # start, end = -1, -1
        #
        # for i, num in enumerate(nums):
        #     if num == target:
        #         if start == -1:
        #             start = i  # Record the first occurrence
        #         end = i        # Keep updating to the latest occurrence
        #
        # return [start, end]

        # Binary Search: O(log n) time, O(1) extra space

        def findFirst():
            left, right = 0, len(nums) - 1
            result = -1  # Store the first occurrence found so far

            while left <= right:
                middle = (left + right) // 2

                if nums[middle] >= target:
                    if nums[middle] == target:
                        result = middle  # Found target; save this index

                    # Search the left half for an earlier occurrence.
                    # Exclude middle because we already checked it.
                    right = middle - 1
                else:
                    # nums[middle] is smaller than target,
                    # so the target must be on the right.
                    left = middle + 1

            return result

        def findLast():
            left, right = 0, len(nums) - 1
            result = -1  # Store the last occurrence found so far

            while left <= right:
                middle = (left + right) // 2

                if nums[middle] <= target:
                    if nums[middle] == target:
                        result = middle  # Found target; save this index

                    # Search the right half for a later occurrence.
                    # Exclude middle because we already checked it.
                    left = middle + 1
                else:
                    # nums[middle] is greater than target,
                    # so the target must be on the left.
                    right = middle - 1

            return result

        # Return the first and last positions of target.
        # If target is absent, the corresponding function returns -1.
        return [findFirst(), findLast()]
