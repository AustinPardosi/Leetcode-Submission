from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count how many times each number appears
        data = defaultdict(int)

        for num in nums:
            data[num] += 1

        # arr[i] contains numbers that appear exactly i times
        # +1 because frequency can be len(nums)
        arr = [[] for _ in range(len(nums) + 1)]

        for num, count in data.items():
            arr[count].append(num)

        # Start from the highest frequency
        result = []

        for i in range(len(arr) - 1, 0, -1):
            for num in arr[i]:
                result.append(num)

                # Stop once we have k numbers
                if len(result) == k:
                    return result