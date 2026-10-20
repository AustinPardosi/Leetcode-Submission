# Brute Force
class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        n = len(nums)

        # Store the closest sum found so far.
        # Infinity ensures the first combination will be accepted.
        closest = float("inf")

        # Choose the first number
        for i in range(n):
            # Choose the second number after i
            for j in range(i + 1, n):
                # Choose the third number after j
                for k in range(j + 1, n):
                    # Calculate the sum of these three numbers
                    total = nums[i] + nums[j] + nums[k]

                    # If this sum is closer to the target,
                    # update our best answer.
                    if abs(total - target) < abs(closest - target):
                        closest = total

                    # If we find an exact match, we cannot
                    # get any closer to the target.
                    if total == target:
                        return total

        return closest

# Two Pointers
class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        # Sort the array so we can move pointers based on the sum.
        nums.sort()

        # Store the closest sum found so far.
        closest = float("inf")

        # Fix the first number of the triplet.
        for i in range(len(nums) - 2):

            # Search for the other two numbers in the remaining array.
            left = i + 1
            right = len(nums) - 1

            while left < right:
                # Calculate the sum using the three selected numbers.
                total = nums[i] + nums[left] + nums[right]

                # Update the closest sum if this sum is nearer to target.
                if abs(total - target) < abs(closest - target):
                    closest = total

                # An exact match is the best possible answer.
                if total == target:
                    return total

                # If the sum is too large, decrease it by moving right left.
                elif total > target:
                    right -= 1

                # If the sum is too small, increase it by moving left right.
                else:
                    left += 1

        return closest