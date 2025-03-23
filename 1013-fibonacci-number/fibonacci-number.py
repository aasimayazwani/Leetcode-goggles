class Solution:
    def fib(self, n: int) -> int:
        dp = {}
        dp[0], dp[1] = 0, 1
        def recurse(n):
            if n in dp:
                return dp[n]
            else:
                dp[n] = recurse(n-1) + recurse(n-2)
                return dp[n]

        return recurse(n)