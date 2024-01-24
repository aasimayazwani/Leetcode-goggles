class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        counting = 0
        for length in range(1,len(nums)+1):
            for left in range(0,len(nums)-length+1):
                current = nums[left:left + length]
                
                counting += len(set(current))**2
                current = current[1:]
        return counting 