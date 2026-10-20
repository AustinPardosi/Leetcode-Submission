class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0

        # Handle the negative exponent by taking the reciprocal
        # of the final result instead of x at the beginning.
        if n < 0:
            return 1 / self.myPow(x, -n)

        half = self.myPow(x, n // 2)
        result = half * half

        if n % 2 == 1:
            result *= x

        return result