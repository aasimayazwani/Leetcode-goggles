class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        limit = len(arr)*0.25
        from collections import Counter
        mapping = Counter(arr)
        return [key for (key,value) in mapping.items() if value > limit][0]