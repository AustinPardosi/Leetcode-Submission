from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        dq = deque()
        result = []

        for i, num in enumerate(nums):
            # Remove the index if it is outside the current window
            if dq and dq[0] <= i - k:
                dq.popleft()
            
            # Remove smaller elements from the back
            # We want the largest value to stay at the front
            while dq and nums[dq[-1]] <= num:
                dq.pop()
            
            # Add the current index
            dq.append(i)

            # Start adding results once the window has size k
            if i >= k - 1:
                result.append(nums[dq[0]])
        return result