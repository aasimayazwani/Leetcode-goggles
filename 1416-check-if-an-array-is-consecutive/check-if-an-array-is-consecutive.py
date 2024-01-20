class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:
        minimum = min(nums)
        result = []
        for i in range(minimum,minimum+len(nums)):
            result.append(i)
        from collections import Counter
        return Counter(result) == Counter(nums)