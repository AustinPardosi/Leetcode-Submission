class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        data = set(nums)
        longest = 0

        for num in data:
            # If num - 1 exists, then num is not the beginning. 
            # Something before it can already start the sequence, so we skip it.
            if num - 1 in data:
                continue
            count = 1
            while num + count in data:
                count += 1
            longest = max(longest, count)
        return longest