class Solution:
    def tribonacci(self, n: int) -> int:
        current = {}
        current[0], current[1], current[2] = 0,1,1

        def result(n):
            if n in current:
                return current[n]
            else:
                current[n] = result(n-3) + result(n-1) + result(n-2) 
                return current[n]
        return result(n)