class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        data = set(nums)
        longest = 0

        for num in data:
            if num - 1 in data:
                continue
            count = 1
            while num + count in data:
                count += 1
            longest = max(longest, count)
        return longest