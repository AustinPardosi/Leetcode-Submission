class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        # Merge Sort
        # Time Complexity: O(n log n) — split the array into halves and merge at each level
        # Space Complexity: O(n) — store temporary arrays while merging

        # Base case: an array with 0 or 1 element is already sorted
        if len(nums) <= 1:
            return nums

        # Divide the array into two halves
        mid = len(nums) // 2

        # Recursively sort the left and right halves
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])

        # Merge the two sorted halves into one sorted array
        result = []
        i, j = 0, 0  # Pointers for the left and right arrays

        # Compare the current elements and add the smaller one to result
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])  # Add the current element from the left
                i += 1                  # Move to the next element in the left array
            else:
                result.append(right[j]) # Add the current element from the right
                j += 1                  # Move to the next element in the right array

        # Add any remaining elements from the left array
        result.extend(left[i:])

        # Add any remaining elements from the right array
        result.extend(right[j:])

        # Return the fully merged and sorted array
        return result