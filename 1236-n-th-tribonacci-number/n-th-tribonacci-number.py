class Solution:
    def tribonacci(self, n: int) -> int:
        mapping = {}
        mapping[0], mapping[1], mapping[2] = 0, 1, 1
        
        def traverse(n):
            if n in mapping:
                return mapping[n]

            else:
                mapping[n] = traverse(n-1) + traverse(n-2) + traverse(n-3)
                return mapping[n]
        return traverse(n)
