class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        from collections import Counter
        mapping = Counter(list(range(0,len(nums)+1)))
        mapping2 = Counter(nums)
        diff = mapping-mapping2
        return list(diff.keys())[0]