class Solution:
    def tribonacci(self, n: int) -> int:
        mapping = {}
        mapping[0] = 0 
        mapping[1] = 1
        mapping[2] = 1

        def looping(n):
            if n in mapping:
                return mapping[n]
            if n not in mapping:
                mapping[n] = looping(n-1) + looping(n-2) + looping(n-3)
                return mapping[n]
        return looping(n)