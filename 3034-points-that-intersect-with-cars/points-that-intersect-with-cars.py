class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        mapping = {}
        for i in range(0,len(nums)):
            for j in range(nums[i][0],nums[i][-1]+1):
                mapping[j] = 1 
        return len(mapping.keys())