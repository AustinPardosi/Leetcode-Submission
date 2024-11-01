class Solution:
    def hammingWeight(self, n: int) -> int:
        result = 0
        binString = bin(n)
        for char in binString:
            if char == "1":
                result += 1

        return result
