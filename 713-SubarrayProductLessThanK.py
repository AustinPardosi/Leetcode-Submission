# Brute Force
# Time:  O(n^2) 
# Space: O(1)
class SolutionBruteForce:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        count = 0

        for i in range(len(nums)):          # start of subarray
            prod = 1
            for j in range(i, len(nums)):   # end of subarray
                prod *= nums[j]
                if prod < k:
                    count += 1
                else:
                    # Positive numbers: the product only grows from here,
                    # so no longer subarray starting at i can be valid.
                    break

        return count

# Sliding Window
# Time:  O(n)
# Space: O(1)
class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        # Every product of positive ints is >= 1, so nothing is < k
        if k <= 1:
            return 0

        l = 0
        count = 0
        product = 1

        for r in range(len(nums)):
            # 1. Expand: bring nums[r] into the window
            product *= nums[r]

            # 2. Shrink: while the product is too big, divide out nums[l]
            #    (exact division, since nums[l] is a factor of prod)
            while product >= k:
                product /= nums[l]
                l += 1

            # 3. Every subarray ending at r inside nums[l..r] is valid
            count += (r - l + 1)
        return count