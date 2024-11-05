class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        arrSet = set()
        duplicate = []

        for num in nums:
            if num in arrSet:
                duplicate.append(num)
            else:
                arrSet.add(num)

        return duplicate
