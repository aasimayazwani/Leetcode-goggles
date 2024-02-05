class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        from collections import Counter
        mapping = Counter(nums)
        return [item[0] for item in mapping.items() if item[1] == 1 ][0]