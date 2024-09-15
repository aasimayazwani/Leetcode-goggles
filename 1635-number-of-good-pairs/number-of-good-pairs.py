class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        collector = []
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j]:
                    collector.append((i,j))
        return len(collector) 