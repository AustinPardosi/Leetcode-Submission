from collections import deque
# Brute Force with BFS but always got Memory Limit
# Time Complexity = O(n^2)
# Space Complexity = O(n^2)
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        target = tuple(range(n))
        start = tuple(nums)

        queue = deque([(start, 0)])
        visited = {start}

        while queue:
            curr, movements = queue.popleft()
            # If the current array is sorted, return the operations used.
            if curr == target:
                return movements

            # Case 1: Reverse the entire array.
            reversed_arr = curr[::-1]
            
            if reversed_arr not in visited:
                visited.add(reversed_arr)
                queue.append((reversed_arr, movements + 1))

            # Case 2: Rotate left by one position.
            rotated_arr = curr[1:] + curr[:1]
            
            if rotated_arr not in visited:
                visited.add(rotated_arr)
                queue.append((rotated_arr, movements + 1))
        return -1

# Best Approach
