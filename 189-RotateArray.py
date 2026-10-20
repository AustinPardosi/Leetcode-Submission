
class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Rotate the array to the right by k steps.
        Modify nums in-place without returning anything.
        """

        # Brute Force: Rotate one step at a time, k times
        # n = len(nums)
        # k %= n  # Rotating n times gives the original array

        # for _ in range(k):
        #     last = nums[-1]  # Save the last element before shifting

        #     # Shift every element one position to the right
        #     for i in range(n - 1, 0, -1):
        #         nums[i] = nums[i - 1]

        #     # Put the previous last element at the beginning
        #     nums[0] = last

        # Time: O(n * k), Space: O(1)

        # Best Approach: Reverse the array in three steps
        n = len(nums)
        k %= n  # Handle k greater than or equal to n

        def reverse(left, right):
            # Swap elements from both ends until they meet
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        # Step 1: Reverse the entire array
        reverse(0, n - 1)

        # Step 2: Reverse the first k elements
        reverse(0, k - 1)

        # Step 3: Reverse the remaining elements
        reverse(k, n - 1)

        # Time: O(n), Space: O(1)
