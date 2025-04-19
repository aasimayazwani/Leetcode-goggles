class Solution:
    def tribonacci(self, n: int) -> int:
        mapping = {}
        mapping[0] = 0
        mapping[1] = 1 
        mapping[2] = 1 
        def search(n):
            if n in mapping:
                return mapping[n]
            else:
                mapping[n] = search(n-1) + search(n-2) + search(n-3)
                return mapping[n]
        return search(n)