class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {}
        dp[1], dp[2] = 1, 2

        def recurse(n):
            if n in dp:
                return dp[n]
            else:
                dp[n] = recurse(n-1) + recurse(n-2)
                return dp[n]
        
        return recurse(n)