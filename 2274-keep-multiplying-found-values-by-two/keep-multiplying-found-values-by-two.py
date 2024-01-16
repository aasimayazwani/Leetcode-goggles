class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        mapping = {}
        for i in range(0,len(nums)):
            mapping[nums[i]] = 1 

        while True:
            if original in mapping:
                original = original*2
            else:
                return original