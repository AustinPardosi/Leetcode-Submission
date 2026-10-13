from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        currSum = 0
        previousCount = defaultdict(int)
        previousCount[0] = 1

        for num in nums:
            currSum += num
            # if currSum - prevSum = K
            # rephrase currSum - k = prevSum
            count += previousCount[currSum - k] # Look for the sum we need
            # update the previousCount
            previousCount[currSum] += 1 # Remember the sum we have now for future ref
        return count
