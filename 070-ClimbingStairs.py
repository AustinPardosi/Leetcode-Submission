class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1
        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp

        return one

### DP APPROACH ####
class Solution:
    def climbStairs(self, n: int) -> int:
        # Base case: 0 or 1 stair has n ways to climb
        if n<2:
            return n
        
        # dp[i] = number of distinct ways to reach stair i
        dp = [0] * (n + 1)
        # Base cases:
        dp[1] = 1  # 1 way to climb 1 stair: take 1 step
        dp[2] = 2  # 2 ways to climb 2 stairs: (1+1) or (2)

        # Calculate the number of ways to reach each stair from 3 to n
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        
        # Return the total number of ways to reach stair n
        return dp[n]