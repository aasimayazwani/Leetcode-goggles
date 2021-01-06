class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return self.summing_minimum(nums)
        
    def summing_minimum(self,nums):
        minimum_sum = 0 
        while nums:
            minimum_sum += min(nums[0],nums[1])
            nums.pop(0)
            nums.pop(0)
        return minimum_sum 
            