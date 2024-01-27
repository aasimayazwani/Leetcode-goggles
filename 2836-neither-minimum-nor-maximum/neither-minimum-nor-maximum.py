class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        result =[item for item in nums if item not in [max(nums),min(nums)]]
        if len(result) > 0:
            return result[0]
        return -1 