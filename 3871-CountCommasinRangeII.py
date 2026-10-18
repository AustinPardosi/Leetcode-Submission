class Solution:
    def countCommas(self, n: int) -> int:
        count = 0
        power = 1000

        while (n >= power):
            count += (n - power + 1)
            power *= 1000
        return count