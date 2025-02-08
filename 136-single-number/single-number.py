class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        from collections import Counter
        mapping = Counter(nums)
        return [key for (key,value) in mapping.items() if value == 1][0]