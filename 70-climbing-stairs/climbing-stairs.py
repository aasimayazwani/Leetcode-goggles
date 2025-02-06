class Solution:
    def climbStairs(self, n: int) -> int:
        mapping = {}
        mapping[1], mapping[2] = 1, 2 
        def fib(n):
            if n in mapping:
                return mapping[n]
            else:
                mapping[n] = fib(n-1) + fib(n-2)
                return mapping[n]
        return fib(n)